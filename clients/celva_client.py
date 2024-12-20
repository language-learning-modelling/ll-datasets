from dataclasses import dataclass

@dataclass
class Config:
    RAW_DATASET_FP: str = "./datasets/CELVA/celva.csv"
    PROCESSED_DATASET_FP: str = None 

    def setup_PROCESSED_DATASET_FP(self):
        if self.__getattribute__("RAW_DATASET_FP") is None:
            raise Exception("Missing raw dataset FP")
        else:
            self.PROCESSED_DATASET_FP = self.RAW_DATASET_FP + ".json.zlib"

            
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
    from utils import load_config, dataclass_to_dict, compress_dict

    
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
    celva_ds.pandas_to_json()
    celva_ds.save_all_instances_as_zlib(config.PROCESSED_DATASET_FP)
