import operator
import re
import sys
import json

import click
from rich.console import Console
from rich.table import Table

from identify_cipher import get_cipher
from statistical_tests import all_stats, binary_random, ioc, shannon_entropy

console = Console()


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.option(
    "-t",
    "--text",
    help="The ciphertext you want to analyze.",
    type=str,
)
@click.option("-n", "--number", help="The top n most likely ciphers to display.", default=5, type=click.IntRange(1, 58))
@click.option("-v", "--verbose", count=True, type=int)
@click.option("-f", "--file", type=click.File("rb"), required=False)
def main(**kwargs):
    """
    Ciphey Analyzer will analyze your ciphertext and run advanced algorithms on it to determine the correct encryption.
    Examples:\n
        Basic Usage: cipher_analyzer.py -t "HOBSZOYTMWELIXBDKOKCTMSBZOKCTGQCLCMFMTOYGNILUMBUILWRHOKBSHTWOUOTOPTBADTWOUOTLCUCTGCULIZBNVOAAKHOAETUKUTUFCSDCLCAILNVMPZBEBQCMUNDAEQSABLCOQBULCYOZAPAXCXHPNNPOSBUOGUCSHKOKCWRCPSYYTCPDHNKBUMTCPDNEAHTYTDNLXBUYOLHMTLBYOPOHOYTDHNKBUMTDNEAHODNNWNPOLBQQFSHADKOKCTGXCTXOPOXNPQTYGSIDNEACQSIDZBQACTYFCUCYTHQUDNUSIDQCPBSZOQDPBXCQCKBINZBZASUKCDNSHKUUTBQAEHTYOSHYOSHTWOUMIQBNKZDUNADFDNVOVANCQTHDBNATWOUMIQBNKZY"
    """

    if kwargs["text"] is None:
        sys.exit("Text input expected. Run 'cipher_identifier.py --help' for help")

    kwargs["text"] = re.sub(r"\s+", "", kwargs["text"].upper())
    basic_stats(kwargs["text"])
    identify_cipher(kwargs["text"], kwargs["number"])


def find_missing_letters(text):
    return [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if letter not in text]


def get_cipher_type(cipher):
    with open("cipher_types.json", "r") as f:
        cipher_types = json.load(f)
    return cipher_types[cipher]["types"][0]


def basic_stats(text):
    text_length = str(len(text))
    text_ioc = str(ioc.get_ioc(text))
    text_entropy = str(shannon_entropy.get_shannon_entropy(text))
    table = Table(title="\nBasic stats")
    table.add_column("Stat", justify="center", style="cyan", no_wrap=True)
    table.add_column("Value", justify="center", style="sky_blue1")
    table.add_row("Length", text_length)
    table.add_row("Number of unique characters", str(len(set(text))))
    table.add_row("Missing letters", str(find_missing_letters(text)))
    table.add_row("IoC", text_ioc)
    table.add_row("Shannon entropy", text_entropy)
    table.add_row("Binary random test", str(binary_random.get_binary_random(text)))
    console.print(table)


def identify_cipher(text, number):
    ciphers = ["6x6bifid", "6x6playfair", "Autokey", "Bazeries", "Beaufort", "CONDI", "Grandpre", "Grandpre10x10", "Gromark", "NihilistSub6x6", "Patristocrat", "Quagmire I", "Quagmire II", "Quagmire III", "Quagmire IV", "Slidefair", "Swagman", "Variant", "Vigenere", "amsco", "bifid", "cadenus", "checkerboard", "cmBifid", "columnar", "compressocrat", "digrafid", "foursquare", "fractionatedMorse", "grille", "homophonic", "keyphrase", "monomeDinome", "morbit", "myszkowski", "nicodemus", "nihilistSub", "nihilistTramp", "numberedKey", "periodicGromark", "phillips", "playfair", "pollux", "porta", "portax", "progressiveKey", "ragbaby", "redefence", "routeTramp", "runningKey", "sequenceTramp", "seriatedPlayfair", "simplesubstitution", "syllabary", "tridigital", "trifid", "trisquare", "twosquare"]
    stats = all_stats.get_all_stats(text)
    scores = [stats["IoC"], stats["MIC"], stats["MKA"], stats["DIC"], stats["EDI"], stats["LR"], stats["ROD"], stats["LDI"], stats["SDD"]]
    num_dev = get_cipher(scores, ciphers)
    num_dev = sorted(num_dev, key=operator.itemgetter(1))

    table = Table(title=f"\nTop {number} most likely ciphers\n(lower is better)")
    table.add_column("Cipher", justify="center", style="cyan", no_wrap=True)
    table.add_column("Score", justify="center", style="sky_blue1")
    table.add_column("Cipher type", justify="center", style="green")
    for i in range(number):
        table.add_row(num_dev[i][0], str(round(num_dev[i][1], 3)))
        #table.add_row(get_cipher_type(num_dev[i][0]))
    console.print(table)


if __name__ == "__main__":
    main()
