from ll_datasets import FCE, EFCAMDAT, CELVA

def download_all():
    fce=FCE()
    fce.download()
    efcamdat=EFCAMDAT()
    efcamdat.download()
    celva=CELVA()
    celva.download()

