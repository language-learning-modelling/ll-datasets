from ll_datasets import FCE, EFCAMDAT, CELVA, TokenizedText, MaskedSentenceStr
import json
import os

def dataclass_to_dict(obj):
    return {k:obj.__getattribute__(k)
            for k in obj.__dataclass_fields__.keys()}

def load_config(config_fp_or_jsonstr):
    if os.path.exists(config_fp_or_jsonstr): 
        with open(config_filepath_or_dictstr) as inpf:
            config = json.load(inpf)
            config = {k.upper(): v for k, v in config.items()}
            return config
    else:
        return { k.upper():v for (k,v) in json.loads(config_fp_or_jsonstr).items() } 

def download_all():
    fce=FCE()
    fce.download()
    efcamdat=EFCAMDAT()
    efcamdat.download()
    celva=CELVA()
    celva.download()

def agreements_to_mlm_sentences(tokenized_text : TokenizedText, MASK_STR="[MASK]") -> [MaskedSentenceStr]:
    '''
        prepares list of masked sentences
        {
            "1": {
                ...
                "tokens": [
                  {
                    "token_str": ,
                    "ud_pos",
                  },
                  ...
                ]
            }
        outputs
        ["[MASK] went to ...","I [MASK] to ..."]
    '''
    masked_sentences = []
    tokens = [d['token']['token_str'] for d in tokenized_text.tokens]
    for token_idx, _ in enumerate(tokens):
        masked_token_sentence = tokens.copy()
        masked_token_sentence[token_idx] = MASK_STR 
        masked_sentences.append(
                MaskedSentenceStr(
                    idx=f"{tokenized_text.text_id}_{token_idx}",
                    text=" ".join(masked_token_sentence)
                )
        )
    return masked_sentences
