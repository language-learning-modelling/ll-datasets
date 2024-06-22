import sys
sys.path.append("../ll_datasets")
from models import ModelsDownloader 
# from .ll_datasets import *

downloader = ModelsDownloader()
downloader.download_direct_link()
