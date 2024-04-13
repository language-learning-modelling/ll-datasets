from datasets import load_dataset
class C4200m:
    def __init__():
        pass

    def download(self, output_folder_fp):
        '''
        downloads the dataset using the huggingface dataset library
        https://huggingface.co/datasets/liweili/c4_200m?row=1
        '''
        dataset = load_dataset("liweili/c4_200m")
        dataset.save_to_disk(output_folder_fp)
