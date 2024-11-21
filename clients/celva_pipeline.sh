# describing the pipeline to process celva from scratch
# install dependencies with poetry - start poetry shell
poetry shell
# copy .env file from my pn repo
# run ./celva_client.py
python3 celva_client.py
## now i have the datasets/CELVA folder 
## i want to run the tokenization
## before running the tokenization i  need to download the UD pipe model using download_udpipe.sh
## then i need to create a split/ and  tokenization_batch/ folder inside the CELVA folder
## cp the splits there in our case "celva.csv.json.zlib"
