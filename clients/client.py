from ll_datasets import *




ef = EFCAMDAT()
#############################################
##  download cleaned_efcamdat from gdrive  ##
##     to "./outputs/EFCAMDAT/" folder     ##
#############################################
ef.download()

#############################################
##      from raw to json file              ##
##                                         ##
#############################################
ef.read_cleaned_efcamdat("../outputs/EFCAMDAT/cleaned_efcamdat.csv")
ef.pandas_to_json()
ef.save_all_instances_json("./outputs/EFCAMDAT/cleaned_efcamdat.json")

#############################################
##      generate subsets of data           ##
##        for fine-tuning                  ##
#############################################
ef.generate_nationality_splits()
ef.generate_proficiency_splits()
ef.generate_proficiencyNationality_splits()

ef.output_mlm_pipeline_file(
        base_filename="./outputs/EFCAMDAT/cleaned_efcamdat_",
        filter_="all"
        )

ef.output_mlm_pipeline_file(
        base_filename="./outputs/EFCAMDAT/cleaned_efcamdat_nationality",
        filter_="nationality"
        )

ef.output_mlm_pipeline_file(
        base_filename="./outputs/EFCAMDAT/cleaned_efcamdat_proficiency",
        filter_="proficiency"
        )

ef.output_mlm_pipeline_file(
        base_filename="./outputs/EFCAMDAT/cleaned_efcamdat_nationality_proficiency",
        filter_="nationality_proficiency"
        )


#############################################
##      generate learner training data     ##
##        for fine-tuning                  ##
#############################################
ef.group_clean_efcamdat_texts_by_learner()
