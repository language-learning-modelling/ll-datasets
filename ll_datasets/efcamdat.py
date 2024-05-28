import gdown
class EFCAMDAT:
    def __init__(self):
        pass

    def download(self):
        '''
        downloads the dataset using the huggingface dataset library
        https://huggingface.co/datasets/liweili/c4_200m?row=1
        '''
        self.download_direct_link_clean_efcamdat()
    def download_direct_link_clean_efcamdat(self):
        url = "https://drive.google.com/"\
                "uc?id="\
                "1lcP9LJB4I1geYHvbZnD0sc-gaPbKyN-G"
        output_filepath="./outputs/EFCAMDAT/cleaned_efcamdat.csv"
        if not os.path.exists(output_filepath):
            os.system(f'mkdir -p ./outputs/EFCAMDAT/;mv -i ./outputs/data/ ./outputs/FCE') 
            gdown.download(
                    url=url,
                    output=output_filepath
                    )
