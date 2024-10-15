from ll_datasets import compress_dict, dataclass_to_dict
from ll_datatypes import Text
from dotenv import dotenv_values
import pandas as pd
import gdown
import os

class CELVA:
    def __init__(self):
        self.config = {
            **dotenv_values(".env"),  # load development variables
            **dotenv_values(".env.shared"),  # load shared development variables
            **dotenv_values(".env.secret"),  # load sensitive variables
            # **os.environ,  # override loaded values with environment variables
        }
        print(self.config)

    def download(self, RAW_DATASET_FP):
        '''
        downloads the dataset using the huggingface dataset library
        https://huggingface.co/datasets/liweili/c4_200m?row=1
        '''
        self.config["RAW_DATASET_FP"] = RAW_DATASET_FP
        self.download_direct_link_celva()

    def download_direct_link_celva(self,):
        url = "https://drive.google.com/"\
                "uc?id="\
                f"{self.config['CELVA_CSV_FILE_GDRIVE_ID']}"
        output_filepath=self.config["RAW_DATASET_FP"]
        output_parent_dir_path = os.path.dirname(self.config["RAW_DATASET_FP"]) 
        expected_downloaded_file = self.config["RAW_DATASET_FP"]# "./datasets/CELVA/celva.csv"
        if not os.path.exists(expected_downloaded_file):
            os.system(f"mkdir -p {output_parent_dir_path}")
            gdown.download(
                    url=url,
                    output=output_filepath
            )

    def download_direct_link_agreement_metrics_celva(self):
        url = "https://drive.google.com/"\
                "uc?id="\
                f"{self.config['CELVA_AGREEMENT_JSON_FILE_GDRIVE_ID']}"
        output_filepath="./datasets/CELVA/celva-predictions.json"
        output_parent_dir_path = "./datasets/CELVA/"
        expected_downloaded_file = "./datasets/CELVA/celva-predictions.json"
        if not os.path.exists(expected_downloaded_file):
            os.system(f"mkdir -p {output_parent_dir_path}")
            gdown.download(
                    url=url,
                    output=output_filepath
            )

    def read_celva_csv_dataset(
                            self,
                            filepath, 
                            targetL2=['Anglais']
                           ):
        dataset = pd.read_csv(filepath)
        print(dataset)
        print(dataset.columns)
        ds_eng = dataset.loc[ dataset['L2'].isin(targetL2) ]
        ds_eng = ds_eng 
        texts = ds_eng['Texte_etudiant'].to_list()
        vocrange = ds_eng['Voc_range'].to_list()
        self.all_instances = dataset.reset_index().to_dict(orient='records')

    def pandas_to_json(self):
        text_objs={}
        for text_dict in self.all_instances:
            text_obj = Text(
                        text_id=text_dict["pseudo"],
                        text=text_dict["Texte_etudiant"],
                        text_metadata={
                                k:v for k,v in text_dict.items()
                                if k not in ["pseudo","Texte_etudiant"]
                            }
                    )
            text_objs[text_obj.text_id] = dataclass_to_dict(text_obj)
        self.all_instances = text_objs

    def save_all_instances_as_zlib(self, output_fp):
        """
        Save the JSON object to a file.

        Parameters
        ----------
        output_fp : str
            The file path to save the JSON data.

        Raises
        ------
        AttributeError
            If the JSON data is not available as attribute 'all_instances'.
        """
        if hasattr(self, 'all_instances'):
            if os.path.exists(output_fp):
                return
            compressed_dataset_dict = compress_dict(self.all_instances)
            with open(output_fp, "wb") as outf:
                outf.write(compressed_dataset_dict)
        else:
            raise Exception("Given file does not exist")
