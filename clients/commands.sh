#!/bin/bash

#python3 -i -W ignore celva_client.py `jo -p INPUT_FP=outputs/CELVA/celva.csv OUTPUT_FP=./outputs/CELVA/splits/celva_texts.json`

# aa ab ac ad ae af ag ah ai aj ak 
# for SPLIT in al am an;
# do
# 	python3 -W ignore jsonify_efcamdat_traintest_splits.py `jo -p INPUT_FP=outputs/EFCAMDAT/splits/train/train_cleaned_efcamdat__all_segment_${SPLIT} OUTPUT_FP=outputs/EFCAMDAT/splits/train_json/train_cleaned_efcamdat__all_segment_${SPLIT}.json`
# done

poetry shell && pip install .. && python3 -i fce_client.py
