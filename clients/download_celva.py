import sys
sys.path.append("../ll_datasets")
from celva import CELVA 
# from .ll_datasets import *

celva_ds = CELVA()
#############################################
##  download cleaned_efcamdat from gdrive  ##
##     to "./outputs/EFCAMDAT/" folder     ##
#############################################
celva_ds.download()
