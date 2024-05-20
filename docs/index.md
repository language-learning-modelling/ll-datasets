# Lists of datasets and preprocessing code for my Phd

## from christopher bryan survey

| Name                  | Description                 | Sents | Toks   | link        |
| :-------------------- | :----------                 | :---- | :---   | :----       |                             
| FCE                   | B1-B2 Exams                 | 33.7k | 530k   |             |
| NUCLE                 | C1 Essays                   | 57.1k | 1.16m  |             |
| CoNLL-2013            | C1 Essays                   | 1.4k  | 29.2k  |             |
| CoNLL-2014            | C1 Essays                   | 1.3k  | 30.1k  |             |
| Lang-8                | A1-C2? Web                  | 1.03m | 11.8m  |             |
| JFLEG                 | A1-C2? Exams                | 1.5k  | 28k    |             |
| W&I+Locness (BEA-2019)| A1-C2 Exams                 | 43.2k | 800k   |             |
| CLC                   | A1-C2 Exams                 | 1.96m | 29.1m  |             |
| EFCamDat              | A1-C2 Exams                 | 4.6m  | 56.8m  |             |
| WikEd                 | Wiki Native                 | 28.5m | 626m   |             |
| AESW                  | C1-native science           | 1.6m  | 35m    |             |
| GMEG                  | B1-B2-Native Exams-Web-wiki | 5.8k  | 122.4k |             |
| CWEB                  | Native-Web                  | 13.5k | 297k   |             |
| GHT                   | Edits Only                  | 353k  |        |             |

## List of datasets
* names
    - EFCAMDAT
    - CFC 
        - FCE
    - NUCL
    - lang-8 corpus
    - ICLE(international corpus of learner english)
    - C4200m (synthetic)

* Gdrive
    I manually uploaded a backup of all datasets here:
    - cyriel efcamdat
    - FCE
    - C4200m

    to add:
    - NUCLE 
    - lang-8 corpus 
    - ALL CLC

    [gdrive](https://drive.google.com/drive/u/0/folders/1G6dw7f83DcP_TOmhiDi4ALvkhOYrNrP3)

* The Efcamdat
    - official website
    - paper [ The EF-Cambridge Open Language Database (EFCamDat)
](https://www.lingref.com/cpp/slrf/2012/paper3100.pdf) 
        
      Jeroen Geertzen, Theodora Alexopoulou, and Anna Korhonen
    - the cleaned Efcamdat
        - paper

* The FCE
    - [website](https://ilexir.co.uk/datasets/index.html)
    - [papers with code](https://paperswithcode.com/sota/grammatical-error-detection-on-fce)
* The c4_200m ungrammatical
    - huggingface [huggingface](https://huggingface.co/datasets/liweili/c4_200m?row=1) 
* SW4ALL: a CEFR-Classified and Aligned Corpus for Language Learning
* [negative language transsfer dataset](https://www.researchgate.net/publication/352365587_Negative_language_transfer_in_learner_English_A_new_dataset)

## List of data annotation tools for ll

* Errant
    [github](https:www.github.com/chrisjbryant/errant)

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
