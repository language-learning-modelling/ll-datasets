from dataclasses import dataclass

@dataclass
class Config:
    INPUT_FP: str = None
    OUTPUT_FP: str = None

    def __post_init__(self):
        for field_key in self.__dataclass_fields__.keys():
            if self.__getattribute__(field_key) is None:
             raise ValueError(f'missing {field_key} config property')

if __name__ == "__main__":
    import sys
    sys.path.append("../ll_datasets")
    import json
    from multiprocessing import Pool
    from efcamdat import EFCAMDAT
    from utils import load_config, dataclass_to_dict
    from ll_datatypes import Text
    
    config_fp_or_jsonstr = "".join(sys.argv[1:])
    config_dict = load_config(config_fp_or_jsonstr) 
    config = Config(**config_dict) 

    ef = EFCAMDAT()
    ef.read_cleaned_efcamdat("./outputs/EFCAMDAT/cleaned_efcamdat.csv")
    ef.pandas_to_json()
    split_dicts = []
    import time
    def search(params):
        data, text = params
        search = [d for d in data if text == d['text_corrected']]
        if len(search) == 0:
            raise Exception(f"ERROR in {text}")
        else:
            return search[0]
        raise Exception(f"NOT RETURNING")

    with open(config.INPUT_FP) as inputf, Pool(8) as p:
        params = [(ef.all_instances, line.replace("\n",""))
                    for line in inputf]
        aligned_data = p.map(search, params)
    #############################################
    ##  download celva from gdrive             ##
    ##     to "./outputs/CELVA/" folder        ##
    #############################################
    text_objs={}
    for text_dict in aligned_data:
        text_obj = Text(
                    text_id=text_dict["writing_id"],
                    text=text_dict["text_corrected"],
                    text_metadata={
                            k:v for k,v in text_dict.items()
                            if k not in ["text_corrected","text"]
                        }
                )
        text_objs[text_obj.text_id] = dataclass_to_dict(text_obj)
    with open(config.OUTPUT_FP,"w") as outf:
        outf.write(json.dumps(text_objs,indent=4))
