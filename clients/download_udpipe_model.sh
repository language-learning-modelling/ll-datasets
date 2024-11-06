#!/bin/bash

MODEL_DIR="./udpipe_models"

if [ ! -d "$MODEL_DIR" ]; then
  mkdir "$MODEL_DIR"
fi

cd "$MODEL_DIR"

curl --remote-name-all https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3131{/english-ewt-ud-2.5-191206.udpipe,/english-partut-ud-2.5-191206.udpipe,/english-lines-ud-2.5-191206.udpipe,/english-gum-ud-2.5-191206.udpipe}
#/german-gsd-ud-2.5-191206.udpipe,\
#/french-spoken-ud-2.5-191206.udpipe,\
#/french-sequoia-ud-2.5-191206.udpipe,\
#/french-gsd-ud-2.5-191206.udpipe,\
#/french-partut-ud-2.5-191206.udpipe,\
#/swedish-lines-ud-2.5-191206.udpipe,\
#/spanish-gsd-ud-2.5-191206.udpipe,\
#/spanish-ancora-ud-2.5-191206.udpipe,
#/swedish-talbanken-ud-2.5-191206.udpipe}
