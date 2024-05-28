import gdown
import os
class FCE:
    def __init__(self):
        pass

    def download(self):
        '''
        downloads the dataset using the huggingface dataset library
        https://huggingface.co/datasets/liweili/c4_200m?row=1
        '''
        self.download_direct_link_fce_zip()
    def download_direct_link_fce_zip(self):
        url = "https://drive.google.com/"\
                "uc?id="\
                "1_ddKA3eTLVcCu7MQT6j0wS15Njdk-rb8"
        output_filepath="./outputs/TLE_treebank_data.zip"
        if not os.path.exists(output_filepath):
            gdown.download(
                    url=url,
                    output=output_filepath
                    )
        os.system(f'unzip {output_filepath} -d ./outputs/;mv -i ./outputs/data/ ./outputs/FCE') 
