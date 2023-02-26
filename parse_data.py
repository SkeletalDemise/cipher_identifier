from statistical_tests import all_stats
from statistics import mean, stdev

# fmt: off
ciphers = ['amsco','autokey','baconian','bazeries','beaufort','bifid','checkerboard','cmbifid','columnar_transposition','condi','digrafid','foursquare','fractionated_morse','grandpre','grille','gromark','gronsfeld','headlines','homophonic','key_phrase','monome_dinome','morbit','myszkowski','nicodemus','nihilist_substitution','null','numbered_key','periodic_gromark','phillips','phillips_rc','plaintext','playfair','pollux','porta','portax','progressive_key','quagmire1','quagmire2','quagmire3','quagmire4','ragbaby','railfence','redefence','route_transposition','running_key','seriated_playfair','slidefair','swagman','tri_square','tridigital','trifid','two_square','variant','vigenere']


# fmt: on
def generate_stats():
    """
    Function to generate statistical data for all cipher samples
    Each ciphertext is on a new line
    """
    ave = []
    std = []
    for cipher in ciphers:
        print(f"Generating stats for {cipher}")
        data = []
        with open(f"data/{cipher}.txt", encoding="utf8") as file:
            for line in file:
                line = line.strip()
                data.append(all_stats.get_all_stats(line)["IOC"])
        ave.append(mean(data))
        std.append(stdev(data))
    print(ave)
    print(std)


generate_stats()
