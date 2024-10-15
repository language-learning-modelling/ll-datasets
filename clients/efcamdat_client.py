if __name__ == "__main__":
    import sys
    sys.path.append("../ll_datasets")
    from efcamdat import EFCAMDAT
    # from .ll_datasets import *

    ef = EFCAMDAT("./.env")
    #############################################
    ##  download cleaned_efcamdat from gdrive  ##
    ##     to "./datasets/EFCAMDAT/" folder     ##
    #############################################
    ef.download()

    #############################################
    ##      from raw to json file              ##
    ##                                         ##
    #############################################
    ef.read_cleaned_efcamdat("./datasets/EFCAMDAT/cleaned_efcamdat.csv")
    ef.pandas_to_json()
    ef.save_all_instances_as_zlib("./datasets/EFCAMDAT/cleaned_efcamdat.csv.json.zlib")

    #############################################
    ##      generate subsets of data           ##
    ##        for fine-tuning                  ##
    #############################################
    '''
    ef.generate_nationality_splits()
    ef.generate_proficiency_splits()
    ef.generate_proficiencyNationality_splits()

    ef.output_mlm_pipeline_file(
            base_filename="./datasets/EFCAMDAT/cleaned_efcamdat_",
            filter_="all"
            )

    ef.output_mlm_pipeline_file(
            base_filename="./datasets/EFCAMDAT/cleaned_efcamdat_nationality",
            filter_="nationality"
            )

    ef.output_mlm_pipeline_file(
            base_filename="./datasets/EFCAMDAT/cleaned_efcamdat_proficiency",
            filter_="proficiency"
            )

    ef.output_mlm_pipeline_file(
            base_filename="./datasets/EFCAMDAT/cleaned_efcamdat_nationality_proficiency",
            filter_="nationality_proficiency"
            )
    '''
    '''

    #############################################
    ##      generate learner training data     ##
    ##        for fine-tuning                  ##
    #############################################
    ef.group_clean_efcamdat_texts_by_learner()

    #############################################
    ##      generate prefix tokens             ##
    ##        to add in LLM vocabulary         ##
    #############################################
    ef.output_prefix_tokens_txt(outputfp="./datasets/EFCAMDAT/prefix_tokens.txt")
    '''
