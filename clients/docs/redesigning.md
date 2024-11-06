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

## we then tokenize the text into a normalized format
    - i need to retrieve the config used here.
    - If i don't have a config file at least i can read the config class
    - I was using batch_process.sh to set the config with jo and passing it to python script 
    - so i was able to know which config i was running through the batch_process.sh
    - {
         text_id:,
         text: ,
         tokens:,
         sentences: ,
         metadata: {
         }
        }
    

## for the MLM pipeline we have
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
