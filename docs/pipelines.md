# learner corpora processing pipeline
here we describe a sequence of steps of processing learner corpora for training LLMs
Technically most of the steps can be changed of order
## Automatic download of raw datasets
If you have a gdrive link to the raw file you can setup a .env file and automatically download it

## converting raw file to standardized compressed json 
There are two aspects of compressing:
    - removing useless characters (such as pretty print) it will still as a json
    - transforming to a compressed format such as gzip (but later we will need to descompress)



# mermaid
```mermaid
graph LR
    hello --> world
    world --> again
    again --> hello
    subgraph target_splits
        split_by_criteria
    end 
```
```mermaid
graph LR
    cleaed_EFCAMDAT@{ shape: cyl } --> norm
    CELVA-SP@{ shape: cyl } --> norm
    FCE@{ shape: cyl } --> norm
    norm --> standardized-json@{ shape: lean-l }
    subgraph target_splits
        split_by_criteria
    end 
    subgraph train_test_split
        training_test_split
    end
    subgraph mlm_pipeline
        tokenization --> Masking_Strategy
        Masking_Strategy --> MLM_training
    end
    subgraph MS_options
      random_vs_pattern_matching
      token_criteria_e.g._ungrammatical
    end
    model((model)) --> mlm_pipeline
    standardized-json --> target_splits
    split_by_criteria --> full-dataset@{ shape: lean-l }
    split_by_criteria --> filter-by-nationality-dataset@{ shape: lean-l }
    full-dataset --> train_test_split
    train_test_split --> train-standardized-json@{ shape: lean-l }
    train_test_split --> test-standardized-json@{ shape: lean-l }
    train-standardized-json --> mlm_pipeline
    Masking_Strategy --> MS_options
    MLM_training --> mlm-model((pre-trained-model))
```
