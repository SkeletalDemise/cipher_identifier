import operator
import re
import sys

import click
from rich.console import Console

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
    stats(kwargs["text"])


def find_missing_letters(text):
    return [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if letter not in text]


def stats(text):
    ciphers = ["6x6bifid", "6x6playfair", "Autokey", "Bazeries", "Beaufort", "CONDI", "Grandpre", "Grandpre10x10", "Gromark", "NihilistSub6x6", "Patristocrat", "Quagmire I", "Quagmire II", "Quagmire III", "Quagmire IV", "Slidefair", "Swagman", "Variant", "Vigenere", "amsco", "bifid", "cadenus", "checkerboard", "cmBifid", "columnar", "compressocrat", "digrafid", "foursquare", "fractionatedMorse", "grille", "homophonic", "keyphrase", "monomeDinome", "morbit", "myszkowski", "nicodemus", "nihilistSub", "nihilistTramp", "numberedKey", "periodicGromark", "phillips", "playfair", "pollux", "porta", "portax", "progressiveKey", "ragbaby", "redefence", "routeTramp", "runningKey", "sequenceTramp", "seriatedPlayfair", "simplesubstitution", "syllabary", "tridigital", "trifid", "trisquare", "twosquare"]
    text_length = len(text)
    text_ioc = ioc.get_ioc(text)
    text_entropy = shannon_entropy.get_shannon_entropy(text)
    console.print("\nBasic stats:")
    console.print(f"Length: {text_length}")
    console.print(
        f"[steel_blue3]Number of unique characters: {len(set(text))}[/steel_blue3]"
    )
    console.print(
        f"[steel_blue3]Missing letters: {find_missing_letters(text)}[/steel_blue3]"
    )
    console.print(f"[steel_blue3]IoC: {text_ioc}[/steel_blue3]")
    console.print(f"[steel_blue3]Shannon entropy: {text_entropy}[/steel_blue3]")
    console.print(
        f"[steel_blue3]Binary random test: {binary_random.get_binary_random(text)}[/steel_blue3]"
    )
    print(all_stats.get_all_stats(text))
    stats = all_stats.get_all_stats(text)
    scores = [stats["IoC"], stats["MIC"], stats["MKA"], stats["DIC"], stats["EDI"], stats["LR"], stats["ROD"], stats["LDI"], stats["SDD"]]
    num_dev = get_cipher(scores, ciphers)
    num_dev = sorted(num_dev, key=operator.itemgetter(1))
    s = ""
    for i in range(len(num_dev)):
        x = float(num_dev[i][1])
        s += f"{num_dev[i][0]} {str(round(x))}" + "\n"
    print(s)
    # console.print(f"\n[steel_blue3]Top 5 most likely ciphers: {top_5}[/steel_blue3]")


if __name__ == "__main__":
    main()
