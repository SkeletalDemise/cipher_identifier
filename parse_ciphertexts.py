import json
from statistics import mean, stdev
from statistical_tests import all_stats

contents = open("data/random_cipher_data.json", encoding="utf8").read()
data = [json.loads(str(item)) for item in contents.strip().split("\n")]

ciphertexts = []
ave = []
std = []
ciphers = [
    "6x6bifid",
    "6x6playfair",
    "Autokey",
    "Bazeries",
    "Beaufort",
    "CONDI",
    "Grandpre",
    "Grandpre10x10",
    "Gromark",
    "NihilistSub6x6",
    "Patristocrat",
    "Quagmire I",
    "Quagmire II",
    "Quagmire III",
    "Quagmire IV",
    "Slidefair",
    "Swagman",
    "Variant",
    "Vigenere",
    "amsco",
    "bifid",
    "cadenus",
    "checkerboard",
    "cmBifid",
    "columnar",
    "compressocrat",
    "digrafid",
    "foursquare",
    "fractionatedMorse",
    "grille",
    "homophonic",
    "keyphrase",
    "monomeDinome",
    "morbit",
    "myszkowski",
    "nicodemus",
    "nihilistSub",
    "nihilistTramp",
    "numberedKey",
    "periodicGromark",
    "phillips",
    "playfair",
    "pollux",
    "porta",
    "portax",
    "progressiveKey",
    "ragbaby",
    "redefence",
    "routeTramp",
    "runningKey",
    "sequenceTramp",
    "seriatedPlayfair",
    "simplesubstitution",
    "syllabary",
    "tridigital",
    "trifid",
    "trisquare",
    "twosquare",
]

stats = {}
mean_test = []

for cipher in ciphers:
    for item in data:
        if item["ciphertype"] == cipher:
            mean_test.append(all_stats.get_all_stats(item["ciphertext"])["SDD"])
    ave.append(mean(mean_test))
    std.append(stdev(mean_test))

print(ave)
print(std)
# average = [stat["SDD"] for stat in stats]
# print(stdev(average))
