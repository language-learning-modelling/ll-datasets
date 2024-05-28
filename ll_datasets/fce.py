from dotenv import dotenv_values
import ll_datasets
import gdown
import os
class FCE:
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
