# Import required libraries and modules
from ll_datasets import decompress_dict
from llm_agreement_metrics import dataset, metrics, models
# import plotext as plt  # Plotext is commented out, likely for plotting, if needed.
import sys
import os
import random
import json
# import numpy as np
import nltk
import time
import spacy_udpipe
import nltk
from tqdm import tqdm
from datetime import datetime
from dataclasses import dataclass

# Dataclass to store configuration parameters
@dataclass
class Config:
    INPUT_FP: str = None  # Path to the input data file
    OUTPUT_FOLDER: str = None  # Directory for saving output files
    UD_MODEL_FP: str = None  # Path to the Universal Dependencies model
    TEXT_COLUMN: str = None  # Column name containing the text data in the input file

    def __post_init__(self):
        """Ensure that all required configuration fields are provided."""
        # Check for any None fields and raise an error if found
        for field_key in self.__dataclass_fields__.keys():
            if self.__getattribute__(field_key) is None:
                raise ValueError(f'Missing {field_key} config property')

# Function to write processed data to a JSON file
def write_obj(data, outfp, batch=True):
    """
    Write processed data to a JSON file.
    
    Args:
        data (list or dict): The data to write.
        outfp (str): The output file path.
        batch (bool): If True, data is processed as a batch, otherwise single data.
    """
    current_stored_dict = {}  # Dictionary to store processed data
    with open(outfp, 'w') as outf:
        # If writing in batch mode
        if batch:
            for data_dict in data:
                data_id = data_dict['text_id']  # Use text_id as the key
                current_stored_dict.update({data_id: data_dict})
        else:
            data_id = data['metadata']['pseudo']  # For non-batch, use the pseudo ID
            current_stored_dict.update({data['metadata']['pseudo']: data})
        # Convert the dictionary to JSON format and write to the file
        updated_dict_str = json.dumps(current_stored_dict, indent=4)
        outf.write(updated_dict_str)

# Main function to process the dataset
def main(config):
    """
    Main script to process input dataset, tokenize text, and make predictions.
    
    Args:
        config (Config): The configuration object containing input/output paths and model info.
    """
    # Record the start time for the script
    main_start = datetime.utcnow()
    print(f'Main script started at: {main_start.year}-{main_start.month}-{main_start.day}_'
          f'{main_start.hour}:{main_start.minute}:{main_start.second}')
    
    # Load the dataset from the specified file path
    # dataset.read_dataset(config.INPUT_FP)
    def read_dataset_zlib_json(filepath):
        with open(filepath, "rb") as inpf:
            decompressed = decompress_dict(inpf.read())
        return decompressed

    row_dicts = read_dataset_zlib_json(config.INPUT_FP)  

    # Start processing and log the timestamp
    start = datetime.utcnow()
    start_str = f'{start.year}-{start.month}-{start.day}_{start.hour}:{start.minute}:{start.second}'
    write_batch = []  # Initialize a list to store processed data for writing
    prediction_batch = []  # Initialize a list to store predictions (unused in this script)
    print('Starting processing at', start_str)

    # Iterate over rows in the dataset
    pbar = tqdm(row_dicts.items())  # Progress bar for iteration
    pbar.set_description(f"{config.INPUT_FILENAME}")
    for text_idx, (text_id, row_dict) in enumerate(pbar):
        # Set up parameters for tokenization
        tokenize_params = {
            "text": row_dict[config.TEXT_COLUMN],  # The text to be tokenized
            "model": config.UD_MODEL  # The UD model used for tokenization
        }
        # Tokenize the text using the dataset's tokenization function
        tokenizedText = dataset.tokenize_text(tokenize_params)
        # Format the tokenized text
        tokenizedText = [{'token_str': t.text, 'ud_pos': t.pos_} for t in tokenizedText]
        
        # Prepare the structure to store information for this particular text
        text_data = {
            "text_id": text_id,
            "text": row_dict[config.TEXT_COLUMN],
            "text_metadata": {k: v for k, v in row_dict["text_metadata"].items() if k != config.TEXT_COLUMN},
            "sentences": [],
            "tokens": []  # This will store token-level data
        }

        # Iterate over each token in the tokenized text
        for token_idx, token in enumerate(tokenizedText):
            # Create a unique ID for each token
            maskedTokenId = f"{text_id}_{token_idx}"

            models_predictions = {}  # Placeholder for model predictions (currently empty)

            # Structure the data for each token, including model predictions
            data = {
                'token': token,
                'predictions': {
                    'maskedTokenId': maskedTokenId,
                    'maskedTokenIdx': token_idx,
                    'maskedTokenStr': token['token_str'],
                    'models': models_predictions  # Predictions will be added here
                }
            }
            text_data["tokens"].append(data)  # Add token-level data to the text data

        # Add processed text data to the batch
        write_batch.append(text_data)

    # If there is any data to write, call write_obj to save it
    if len(write_batch) > 0:
        write_obj(write_batch, outfp=config.OUTPUT_FP, batch=True)
        write_batch = []  # Reset the write batch after saving data

# Entry point for the script when executed directly
if __name__ == '__main__':
    from ll_datasets import load_config, dataclass_to_dict  # Utility functions for loading config

    # Read config from the command line argument (either a file path or a JSON string)
    config_fp_or_jsonstr = "".join(sys.argv[1:])
    config_dict = load_config(config_fp_or_jsonstr)  # Load the config dictionary
    config = Config(**config_dict)  # Convert the config dictionary to a Config object

    # Load the Universal Dependencies model using spacy_udpipe
    ud_model = spacy_udpipe.load_from_path(lang="en", path=config.UD_MODEL_FP, meta={"description": "A4LL suggested model"})
    config.UD_MODEL = ud_model  # Set the model in the config

    # Derive input/output file names based on the provided paths
    config.INPUT_FILENAME = config.INPUT_FP.split('/')[-1]  # Extract the filename from the input path
    config.OUTPUT_FP = f'{config.OUTPUT_FOLDER}/{config.INPUT_FILENAME}'  # Set the output file path

    print(config)
    # Call the main function with the loaded configuration
    main(config)
