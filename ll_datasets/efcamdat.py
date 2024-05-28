"""
EFCAMDAT Module
===============

This module provides functionality to download, read, process, and save the EFCAMDAT dataset.
The dataset is downloaded from a specified Google Drive link, and the processed data can be saved
in JSON format for further use.

Classes:
--------
EFCAMDAT: A class to manage the EFCAMDAT dataset operations.

Usage:
------
Instantiate the EFCAMDAT class and use its methods to download, read, process, and save the dataset.

Example:
--------
>>> efcamdat = EFCAMDAT()
>>> efcamdat.download()
>>> efcamdat.read_clean_efcamdat()
>>> efcamdat.pandas_to_json()
>>> efcamdat.save_all_instances_json('output.json')
>>> efcamdat.load_json('output.json')
"""

from dotenv import dotenv_values
import gdown
import os
import pandas as pd
import json
import collections

class EFCAMDAT:
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

    def download(self):
        '''
        downloads the dataset using the huggingface dataset library
        https://huggingface.co/datasets/liweili/c4_200m?row=1
        '''
        self.download_direct_link_clean_efcamdat()

    def download_direct_link_clean_efcamdat(self):
        """
        Download the cleaned EFCAMDAT dataset from a direct Google Drive link.

        If the dataset file does not already exist, it is downloaded and saved to the specified path.
        """
        url = "https://drive.google.com/"\
                "uc?id="\
                f"{self.config['EFCAMDAT_CSV_FILE_GDRIVE_ID']}"
        output_filepath="./outputs/EFCAMDAT/cleaned_efcamdat.csv"
        output_parent_dir_path = "./outputs/EFCAMDAT/"
        expected_downloaded_file = "./outputs/EFCAMDAT/cleaned_efcamdat.csv"
        if not os.path.exists(expected_downloaded_file):
            os.system(f"mkdir -p {output_parent_dir_path}")
            gdown.download(
                    url=url,
                    output=output_filepath
            )

    def read_clean_efcamdat(self, filepath=None):
        """
        Read the cleaned EFCAMDAT dataset from a CSV file.

        Parameters
        ----------
        filepath : str, optional
            The file path to the CSV file. If not provided, it will use the path from the configuration.

        Raises
        ------
        Exception
            If the file does not exist.
        """
        if filepath == None \
                and self.config.get('CLEAN_EFCAMDAT_CSV_FILEPATH', False):
            filepath =  self.config['CLEAN_EFCAMDAT_CSV_FILEPATH']
        if not os.path.exists(filepath):
            raise Exception("Given file does not exist")
        self.dataframe = pd.read_csv(filepath)

    def pandas_to_json(self):
        """
        Convert the pandas DataFrame to a JSON object.

        The DataFrame is converted to a dictionary with records orientation.
        """
        self.instances_dict = json.loads(self.dataframe.to_json(orient="records"))

    def save_all_instances_json(self, output_fp):
        """
        Save the JSON object to a file.

        Parameters
        ----------
        output_fp : str
            The file path to save the JSON data.

        Raises
        ------
        AttributeError
            If the JSON data is not available as attribute 'instances_dict'.
        """
        if hasattr(self, 'instances_dict'):
            json_formatted_str = json.dumps(self.instances_dict, indent=4)
            with open(output_fp, "w") as outf:
                outf.write(json_formatted_str)

    def load_json(self, filepath=None):
        """
        Load JSON data from a file or .ENV config .

        Parameters
        ----------
        filepath : str
            The file path to the JSON file. If not provided, it will use the path from the configuration.

        Raises
        ------
        Exception
            If the file does not exist.
        """
        if filepath == None \
                and self.config.get('CLEAN_EFCAMDAT_JSON_FILEPATH', False):
            filepath =  self.config['CLEAN_EFCAMDAT_JSON_FILEPATH']
        if not os.path.exists(filepath):
            raise Exception("Given file does not exist")
        with open(filepath) as inpf:
            self.instances_dict = json.load(inpf)

    def generate_nationality_splits(self):
        self.unique_nationalities = collections.defaultdict(int)
        self.nationalities_instances = collections.defaultdict(list)
        for d in self.instances_dict:
            self.unique_nationalities[d['nationality']] += 1 
            self.nationalities_instances[d['nationality']].append(d)
        self.unique_nationalities = {k:v for k,v in sorted(
                                        self.unique_nationalities.items(),
                                        key=lambda tpl: tpl[1]
                                        )}
        print(self.unique_nationalities)

    def generate_proficiency_splits(self):
        self.unique_proficiencies = collections.defaultdict(int)
        self.nationalities_instances = collections.defaultdict(list)
        for d in self.instances_dict:
            self.unique_proficiencies[d['cefr']] += 1 
            self.nationalities_instances[d['cefr']].append(d)
        self.unique_proficiencies = {k:v for k,v in sorted(
                                        self.unique_proficiencies.items(),
                                        key=lambda tpl: tpl[1]
                                        )}
        print(self.unique_proficiencies)

    def generate_proficiencyNationality_splits(self):
        self.unique_nationalities_proficiency_pairs = collections.defaultdict(int)
        self.nationalities_proficiencies_instances = collections.defaultdict(list)
        for d in self.instances_dict:
            nationality_proficiency_pair = f"{d['cefr']}_{d['nationality']}"
            self.unique_nationalities_proficiency_pairs[nationality_proficiency_pair] += 1 
            self.nationalities_proficiencies_instances[nationality_proficiency_pair].append(d)
        self.unique_nationalities_proficiency_pairs = {k:v for k,v in sorted(
                                        self.unique_nationalities_proficiency_pairs.items(),
                                        key=lambda tpl: tpl[1]
                                        )}
        print(self.unique_nationalities_proficiency_pairs)

    def generate_specific_learner_split(self, learner_id):
        pass

    def output_mlm_pipeline_file(self, output_fp):
        for nationality, instances_lst in self.nationalities_instances.items():
                nationality_fp=f'{output_fp.replace(".txt","")}_{nationality}.txt'
                texts="\n".join([d["text_corrected"] for d in instances_lst])
                with open(nationality_fp, "w") as outf:
                    outf.write(texts)


