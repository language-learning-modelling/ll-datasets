import gdown

def download_direct_link_processed_selva():
    url = "https://drive.google.com/"\
            "uc?id="\
            "1MoEBn7Er3BuR47tB9n2GIPkqVr0Yl7Kf"
    output_filepath="./outputs/celva_full_processed.json"
    gdown.download(
            url=url,
            output=output_filepath
            )

download_direct_link_processed_selva()
