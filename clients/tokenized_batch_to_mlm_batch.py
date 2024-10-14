from dataclasses import dataclass

@dataclass
class Config:
    INPUT_FP: str = None
    OUTPUT_FOLDER: str = None

    def __post_init__(self):
        for field_key in self.__dataclass_fields__.keys():
            if self.__getattribute__(field_key) is None:
             raise ValueError(f'missing {field_key} config property')

if __name__ == "__main__":
    import sys
    import json
    sys.path.insert(0,"../ll_datasets")
    from ll_datatypes import TokenizedText, MaskedSentenceStr
    from utils import agreements_to_mlm_sentences, load_config

    config_fp_or_jsonstr = "".join(sys.argv[1:])
    config_dict = load_config(config_fp_or_jsonstr) # if input is json str 
    ### if input is fp ### config_dict = load_config(config_fp_or_jsonstr)
    config = Config(**config_dict) 
    input_filename = config.INPUT_FP.split("/")[-1]
    output_fp = config.OUTPUT_FOLDER + "/" + input_filename + "_maskedsentences.json" 
    texts_objs = {k:TokenizedText(**d) for k,d in json.load(open(config.INPUT_FP)).items()} 
    with open(output_fp,"w") as outf:
        for text_idx, text_obj in enumerate(texts_objs.values()):
            maskedsentences_objs = agreements_to_mlm_sentences(text_obj)    
            for token_idx, maskedsentence_obj in enumerate(maskedsentences_objs):
                texts_objs[text_obj.text_id].tokens[token_idx]['predictions']['maskedSentence'] = {
                            'maskedSentenceStr': maskedsentence_obj.text
                        }
        output_dict = {
            text_obj.text_id: {
                field_key: text_obj.__getattribute__(field_key)
                for field_key in text_obj.__dataclass_fields__.keys()
            } for text_idx, text_obj in enumerate(texts_objs.values())
        }
        dict_str = json.dumps(output_dict,indent=4)
        outf.write(dict_str)
