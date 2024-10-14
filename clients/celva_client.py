from dataclasses import dataclass

@dataclass
class Config:
    RAW_DATASET_FP: str = "./datasets/CELVA/celva.csv"
    PROCESSED_DATASET_FP: str = None 

    def setup_PROCESSED_DATASET_FP(self):
        if self.__getattribute__("RAW_DATASET_FP") is None:
            raise Exception("Missing raw dataset FP")
        else:
            self.PROCESSED_DATASET_FP = self.RAW_DATASET_FP + ".json"

            
    def __post_init__(self):
        self.setup_PROCESSED_DATASET_FP()
        for field_key in self.__dataclass_fields__.keys():
            if self.__getattribute__(field_key) is None:
             raise ValueError(f'missing {field_key} config property')

if __name__ == "__main__":
    import sys
    sys.path.append("../ll_datasets")
    from celva import CELVA 
    import json
    from utils import load_config, dataclass_to_dict
    from ll_datatypes import Text
    
    config_fp_or_jsonstr = "".join(sys.argv[1:])
    if config_fp_or_jsonstr:
        config_dict = load_config(config_fp_or_jsonstr) 
        config = Config(**config_dict) 
    else:
        input("You gave an empty config, proceed ?")
        config = Config(**{"RAW_DATASET_FP": "./datasets/CELVA/celva.csv"})
    celva_ds = CELVA()
    #############################################
    ##  download celva from gdrive             ##
    ##     to "./outputs/CELVA/" folder        ##
    #############################################
    celva_ds.download(config.RAW_DATASET_FP)
    #### ENGLISH ONLY text
    celva_ds.read_celva_csv_dataset(config.RAW_DATASET_FP)
    text_objs={}
    for text_dict in celva_ds.records:
        text_obj = Text(
                    text_id=text_dict["pseudo"],
                    text=text_dict["Texte_etudiant"],
                    text_metadata={
                            k:v for k,v in text_dict.items()
                            if k not in ["pseudo","Texte_etudiant"]
                        }
                )
        text_objs[text_obj.text_id] = dataclass_to_dict(text_obj)
    with open(config.PROCESSED_DATASET_FP,"w") as outf:
        outf.write(json.dumps(text_objs,indent=4))
