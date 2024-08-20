import os
from dataclasses import dataclass
from dotenv import dotenv_values
from conllu import parse
import gdown
import ll_datasets

@dataclass
class FCEConfig:
    INPUT_FOLDER: str = None

    def __post_init__(self):
        print(dir(self)) 
        exit()

class FCE:
    def __init__(self, config):
        self.config = {
            **dotenv_values(".env"),  # load development variables
            **dotenv_values(".env.shared"),  # load shared development variables
            **dotenv_values(".env.secret"),  # load sensitive variables
        }

    def download(self):
        '''
        '''
        self.download_direct_link_fce_zip()

    def download_direct_link_fce_zip(self):
        url = "https://drive.google.com/"\
                "uc?id="\
                f"{self.config['FCE_ZIP_FILE_GDRIVE_ID']}"
        output_filepath="./outputs/TLE_treebank_data.zip"
        output_parent_dir_path = "./outputs/"
        expected_extracted_dir_from_zip = "./outputs/data/"
        os.system(f"mkdir -p {output_parent_dir_path}")
        if not os.path.exists(output_filepath):
            gdown.download(
                    url=url,
                    output=output_filepath
                    )
        os.system(f'unzip {output_filepath} -d {output_parent_dir_path};mv -i {expected_extracted_dir_from_zip} ./outputs/FCE') 

    def parse_raw_fce(self):
        with open("./outputs/FCE/en_esl-ud-train.conllu") as original_inpf:
            self.original_data = parse(original_inpf.read())
            self.corrected_data = parse(original_inpf.read())
        with open("./outputs/FCE/corrected/en_cesl-ud-train.conllu") as original_inpf:
            for 



