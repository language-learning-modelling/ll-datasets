from ll_datasets import FCE

processingConfig = {
        "input_folder": "./outputs/FCE"
        }
client = FCE(processingConfig)
#client.download()

client.parse_raw_fce()


