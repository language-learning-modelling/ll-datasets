import json
import collections

# ./outputs/samples/celva/tnc_bertbaseuncased_celva.json
# ./outputs/samples/tnc_c4200m_celva_30_sample.json
filename="./outputs/CELVA/masked_sentences_batch/processed/celva_texts.json_maskedsentences.json" 

#"celva_texts.json_maskedsentences.json_bert-base-uncased-c4200m-unchaged-vocab-73640000.json"
# "celva_texts.json_maskedsentences.json_bert-base-uncased.json"
# "celva_texts.json_maskedsentences.json_bert-base-uncased-c4200m-unchaged-vocab-73640000.json"
# "celva_texts.json_maskedsentences.json_bert-base-uncased-finetuned-cleaned_efcamdat__all.txt_checkpoint-464970.json"
#inputfp=f"/home/berstearns/projects/language-learning-modelling/selva-agreement-metrics/selva-agreement-clients/poetry-client/outputs/CELVA/finalized/{filename}"
inputfp=filename
#target_model_name="bert-base-uncased-c4200m-unchaged-vocab-73640000"
# "bert-base-uncased"
# "bert-base-uncased-c4200m-unchaged-vocab-73640000"
# "bert-base-uncased-finetuned-cleaned_efcamdat__all.txt_checkpoint-464970"
#"bert-base-uncased"
with open(inputfp) as inpf:
    text_dicts_dict = json.load(inpf)
    for text_id, text_dict in text_dicts_dict.items(): 
        for token_idx, token_dict in enumerate(text_dict["tokens"]):
            del text_dicts_dict[text_id]["tokens"][token_idx]["predictions"]["maskedSentence"] 
    with open("reduced_json.json","w") as outf:
        outf.write(json.dumps(text_dicts_dict,indent=4))
