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
    def __init__(self, env_filepath=".env"):
        """
        Initialize the EFCAMDAT class by loading configuration variables from environment files.
        """
        self.config = {
            **dotenv_values(env_filepath),  # load development variables
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
        output_filepath="./datasets/EFCAMDAT/cleaned_efcamdat.csv"
        output_parent_dir_path = "./datasets/EFCAMDAT/"
        expected_downloaded_file = "./datasets/EFCAMDAT/cleaned_efcamdat.csv"
        if not os.path.exists(expected_downloaded_file):
            os.system(f"mkdir -p {output_parent_dir_path}")
            gdown.download(
                    url=url,
                    output=output_filepath
            )

    def read_cleaned_efcamdat(self, filepath=None):
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
        if not hasattr(self, "dataframe"):
            try:
                self.read_clean_efcamdat()
            except:
                raise Exception("Run efcamdat.read_clean_efcamdat first")
        self.all_instances = json.loads(self.dataframe.to_json(orient="records"))

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
            If the JSON data is not available as attribute 'all_instances'.
        """
        if hasattr(self, 'all_instances'):
            if os.path.exists(output_fp):
                return
            json_formatted_str = json.dumps(self.all_instances, indent=4)
            with open(output_fp, "w") as outf:
                outf.write(json_formatted_str)
        else:
            raise Exception("Given file does not exist")

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
            self.all_instances = json.load(inpf)

    def generate_nationality_splits(self):
        self.unique_nationality = collections.defaultdict(int)
        self.nationality_instances = collections.defaultdict(list)
        for d in self.all_instances:
            self.unique_nationality[d['nationality']] += 1 
            self.nationality_instances[d['nationality']].append(d)
        self.unique_nationality = {k:v for k,v in sorted(
                                        self.unique_nationality.items(),
                                        key=lambda tpl: tpl[1]
                                        )}
        print(self.unique_nationality)

    def generate_proficiency_splits(self):
        self.unique_proficiency = collections.defaultdict(int)
        self.proficiency_instances = collections.defaultdict(list)
        for d in self.all_instances:
            self.unique_proficiency[d['cefr']] += 1 
            self.proficiency_instances[d['cefr']].append(d)
        self.unique_proficiency = {k:v for k,v in sorted(
                                        self.unique_proficiency.items(),
                                        key=lambda tpl: tpl[1]
                                        )}
        print(self.unique_proficiency)

    def generate_proficiencyNationality_splits(self):
        self.unique_nationality_proficiency_pairs = collections.defaultdict(int)
        self.nationality_proficiency_instances = collections.defaultdict(list)
        for d in self.all_instances:
            nationality_proficiency_pair = f"{d['cefr']}_{d['nationality']}"
            self.unique_nationality_proficiency_pairs[nationality_proficiency_pair] += 1 
            self.nationality_proficiency_instances[nationality_proficiency_pair].append(d)
        self.unique_nationality_proficiency_pairs = {k:v for k,v in sorted(
                                        self.unique_nationality_proficiency_pairs.items(),
                                        key=lambda tpl: tpl[1]
                                        )}
        print(self.unique_nationality_proficiency_pairs)

    def group_clean_efcamdat_texts_by_learner(self):
        self.texts_by_learner = collections.defaultdict(lambda : 
            { 
                "texts":[]
            }
        )
        for instance_dict in self.all_instances:
            self.texts_by_learner[instance_dict['learner_id']]['texts'].append(instance_dict)
        for learner_id, learner_dict in self.texts_by_learner.items():
            self.texts_by_learner[learner_id]['n_of_texts'] =\
                len(self.texts_by_learner[learner_id]['texts'])  
        self.texts_by_learner = dict(
                sorted(
                        self.texts_by_learner.items(),key=lambda tpl: tpl[1]['n_of_texts']  
                      ) 
                )
                
    def stats_learners_over_n_texts(self, n):
        stats = {
            "learners_id": [],
            "count": 0,
            "n_texts": 0
        }
        for learner_id, learner_dict in self.texts_by_learner.items():
            if learner_dict["n_of_texts"] >= n:
                 stats['count']+=1
                 stats['n_texts']+=learner_dict["n_of_texts"]
                 stats['learners_id'].append(learner_dict)
        return stats 
            
    def filter_learners_by_n_of_texts(self, n):
        pass 

    def output_prefix_tokens_txt(self, outputfp):
        with open(outputfp, "w") as outf:
            for proficiency_str in self.unique_proficiency:
                outf.write(f"[{proficiency_str.upper()}]"+"\n")

            for nationality_str in self.unique_nationality:
                outf.write(f"[{nationality_str.upper()}]"+"\n")

    def output_mlm_pipeline_file(self,
                                 base_filename,
                                 filter_="proficiency"):
        instances_map = {
            "proficiency": self.proficiency_instances 
                    if hasattr(self, "proficiency_instances") else None,
            "nationality": self.nationality_instances
                    if hasattr(self, "nationality_instances") else None,
            "nationality_proficiency": self.nationality_proficiency_instances
                    if hasattr(self, "nationality_proficiency_instances") else None,
            "all": {"all":self.all_instances}
                    if hasattr(self, "all_instances") else None,
        }
        if not instances_map.get(filter_,False):
            raise Exception("the type of instances you asked for does not exist, try running generate_splits")
        for category_name, instances_lst in instances_map[filter_].items():
                category_name_fp=f'{base_filename.replace(".txt","")}_{category_name}.txt'
                if os.path.exists(category_name_fp):
                    continue
                texts="\n".join([d["text_corrected"] for d in instances_lst])
                with open(category_name_fp, "w") as outf:
                    outf.write(texts)
