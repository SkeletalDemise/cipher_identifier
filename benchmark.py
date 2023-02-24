"""
Benchmark cipher identification accuracy
"""

import json
import operator

from identify_cipher import get_cipher
from statistical_tests import all_stats


def benchmark():
    """
    Function to benchmark the accuracy of the cipher identification algorithm
    """
    contents = open("data/random_cipher_data.json", encoding="utf8").read()
    data = [json.loads(str(item)) for item in contents.strip().split("\n")]

    # fmt: off
    ciphers = ["6x6bifid", "6x6playfair", "Autokey", "Bazeries", "Beaufort", "CONDI", "Grandpre", "Grandpre10x10", "Gromark", "NihilistSub6x6", "Patristocrat", "Quagmire I", "Quagmire II", "Quagmire III", "Quagmire IV", "Slidefair", "Swagman", "Variant", "Vigenere", "amsco", "bifid", "cadenus", "checkerboard", "cmBifid", "columnar", "compressocrat", "digrafid", "foursquare", "fractionatedMorse", "grille", "homophonic", "keyphrase", "monomeDinome", "morbit", "myszkowski", "nicodemus", "nihilistSub", "nihilistTramp", "numberedKey", "periodicGromark", "phillips", "playfair", "pollux", "porta", "portax", "progressiveKey", "ragbaby", "redefence", "routeTramp", "runningKey", "sequenceTramp", "seriatedPlayfair", "simplesubstitution", "syllabary", "tridigital", "trifid", "trisquare", "twosquare"]

    # fmt: on
    correct = 0
    for item in data:
        stats = all_stats.get_all_stats(item["ciphertext"])
        scores = [
            stats["IoC"],
            stats["MIC"],
            stats["MKA"],
            stats["DIC"],
            stats["EDI"],
            stats["LR"],
            stats["ROD"],
            stats["LDI"],
            stats["SDD"],
        ]
        num_dev = get_cipher(scores, ciphers)
        num_dev = sorted(num_dev, key=operator.itemgetter(1))

        # see if correct cipher is in top 5
        for guess in num_dev[:1]:
            if guess[0] == item["ciphertype"]:
                correct += 1
    total_ciphertexts = len(data)
    print(f"\n{correct}/{total_ciphertexts} correct")
    print(f"{correct / total_ciphertexts * 100:.2f}% accuracy")


benchmark()
