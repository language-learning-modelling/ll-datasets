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
    from c4200m import C4200m 
    import json
    from utils import load_config, dataclass_to_dict, compress_dict
    client = C4200m()

    client.download(output_folder_fp="./datasets/C4200m/")
    
