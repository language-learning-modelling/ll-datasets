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

    def download(self):
        '''
        downloads the dataset using the huggingface dataset library
        https://huggingface.co/datasets/liweili/c4_200m?row=1
        '''
        self.download_direct_link_celva()

    def download_direct_link_celva(self):
        url = "https://drive.google.com/"\
                "uc?id="\
                f"{self.config['CELVA_CSV_FILE_GDRIVE_ID']}"
        output_filepath="./outputs/CELVA/celva.csv"
        output_parent_dir_path = "./outputs/CELVA/"
        expected_downloaded_file = "./outputs/CELVA/celva.csv"
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
        output_filepath="./outputs/CELVA/celva-predictions.json"
        output_parent_dir_path = "./outputs/CELVA/"
        expected_downloaded_file = "./outputs/CELVA/celva-predictions.json"
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
        ds_eng = dataset.loc[ dataset['L2'].isin(targetL2) ]
        ds_eng = ds_eng 
        texts = ds_eng['Texte_etudiant'].to_list()
        vocrange = ds_eng['Voc_range'].to_list()
        records = dataset.reset_index().to_dict(orient='records')
        self.records = records
