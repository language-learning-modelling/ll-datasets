# User has a learner corpora
## it can be :
        1) local:
           - a single file
                - csv
                - json
                - txt
                - compressed
           - a batch folder
                - csv
                - json
                - txt
                - compressed
        2) remote
           - a single file
                - csv
                - json
                - txt
                - compressed
           - a batch folder
                - csv
                - json
                - txt
                - compressed

## we normalize to a single common format :
    - normalzing json.zlib
    - I need to describe the schema of it in more details but:  
        - {
         text_id:,
         text: ,
         metadata: {
         }
        }
    - I have the normalized files for EFCADMAT and celva
    - a learner format would be 
        learner_id : {
            texts: [],
            exercises: []
        }

## we then HUMAN tokenize the text into a normalized format
    - i need to retrieve the config used here.
    - If i don't have a config file at least i can read the config class
    - I was using batch_process.sh to set the config with jo and passing it to python script 
    - so i was able to know which config i was running through the batch_process.sh
    - The udpipe model folder with file is not there, how can i download it ?
        - clone the code from A4LL (cyriel) to download model
        - https://gitlab.huma-num.fr/lidile/A4LL_system.git
    - there is a mismatch in the folder structure the efcamdat client is generating and the folder tokenization_batch_processing is expecting
    - I manually fixed this mismtach by coping celva.csv.json.zlib to /CELVA/splits
    - Now i need to make sure the pipleine can read a json.zlib format
    - The code part that reads a file:
        - row_dicts = dataset.read_dataset(config.INPUT_FP)
        - using from llm_agreement_metrics import dataset, metrics, models
        - later on i can move this dataset module to ll-datasets lib
        - it checks the INPUT_FP ending for decide with reading strategy to use:
            - .csv
                - read_pandas
            - .json
                - read_json
            - else
                - read_txt
        - client is fine passing a file ending ".json.zlib", dev needs to address this in code
        - the dev needs to get a .json.zlib read it as bytes and use "decompress_data"
 
    - {
         text_id:"12124",
         text:"das" ,
         tokens:{
         },
         sentences:{} ,
         metadata: {
         }
        }
    
## Human Masked Token Annotation
### HMTA is done as a test procedure for our models
### also for simulation on new learner texts
### for this pipeline in using the mlml repo
### i'm having the same issue of retrieving a run_config file.
###  but as the client I can take a look at the batch_process.sh and i can look into the config class and have some idea
###  CONFIG=$(jo -p input_fp=$FILEPATH output_folder=$OUTPUT_BATCH_FOLDER model_checkpoint=$MODEL_CHECKPOINT batch_size=$BATCH_SIZE top_k=$TOP_K)
### in the batch i can retrieve the examples coonfig
    SPLIT=""
    DATASET="CELVA"
    INPUT_BATCH_FOLDER="./datasets/${DATASET}/tokenization_batch"
    OUTPUT_BATCH_FOLDER="./datasets/${DATASET}/predictions_batch"
    MODEL_NAME="ert-base"
    MODEL_CHECKPOINT="./models/${MODEL_NAME}"
### it requires the model download locally
### how i donwload a model ?
#### we have a download_client.py in the mlml repo a we can find a example config in run_configs


## for the MLM pipeline we have 
    - The mlm pipeline does not require the human tokenizatiion pipeline
    - It just reuires to pass a batch of text
    1) training
        - training is simply using the data collator (default bert training config)

    2) testing  
        - testing is simply for each human token of the given token:
            1) mask one at a time, and try to predict it
            2) mask contigous bigrams one at a time, and try to predict it

## for the CEFR classification pipeline we have:
   1) training
        
   2) testing 
        text as input -> cefr

## GEC
## GED
## SemanticErrorPrediction
