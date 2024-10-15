if __name__ == "__main__":
    import json
    from ll_datasets import compress_dict
    # Sample dictionary
    my_dict = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland",
        "hobbies": ["reading", "adventures", "tea parties"]
    }
    with open("./datasets/EFCAMDAT/cleaned_efcamdat.json") as inpf:
        my_dict = json.load(inpf)

    # Compress the dictionary
    compressed = compress_dict(my_dict)
    with open("./datasets/EFCAMDAT/cleaned_efcamdat.pycompressed.json","wb") as outf:
        outf.write(compressed)
    #print("Compressed data:", compressed)
    # Decompress the dictionary
    # decompressed = decompress_dict(compressed)

