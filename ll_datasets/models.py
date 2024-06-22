from dotenv import dotenv_values
import gdown
import os

class ModelsDownloader:
    def __init__(self):
        """
        Initialize the EFCAMDAT class by loading configuration variables from environment files.
        """
        self.config = {
            **dotenv_values(".env"),  # load development variables
            **dotenv_values(".env.shared"),  # load shared development variables
            **dotenv_values(".env.secret"),  # load sensitive variables
            # **os.environ,  # override loaded values with environment variables
        }

    def download_direct_link(self):
        """
        Download the model folder from a direct Google Drive link.

        If the model folder does not already exist, it is downloaded and saved to the specified path.
        """
        url = "https://drive.google.com/"\
                "uc?id="\
                f"{self.config['BERT_BASE_UNCASED_FULLEFCAMDAT']}"
        output_filepath="./outputs/models/bert-base-uncased-fullefcamdat"
        output_parent_dir_path = "./outputs/models/"
        expected_downloaded_folder = "./outputs/models/bert-base-uncased-full-efcamdat"
        os.system(f"mkdir -p {output_parent_dir_path}")
        gdown.download_folder(
                id=f"{self.config['BERT_BASE_UNCASED_FULLEFCAMDAT']}",
                output=output_filepath
        )
