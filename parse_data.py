from statistical_tests import all_stats
import os

# fmt: off
ciphers = ['numbered_key', 'foursquare', 'porta', 'running_key', 'route_transposition', 'bazeries', 'grille', 'playfair', 'pollux', 'tri_square', 'plaintext', 'slidefair', 'redefence', 'quagmire4', 'amsco', 'gronsfeld', 'seriated_playfair', 'variant', 'swagman', 'gromark', 'null', 'cmbifid', 'periodic_gromark', 'cadenus', 'quagmire3', 'fractionated_morse', 'railfence', 'tridigital', 'trifid', 'vigenere', 'nihilist_substitution', 'monome_dinome', 'nicodemus', 'phillips', 'phillips_rc', 'progressive_key', 'headlines', 'portax', 'condi', 'ragbaby', 'quagmire2', 'morbit', 'quagmire1', 'autokey', 'beaufort', 'bifid', 'two_square', 'homophonic', 'checkerboard', 'baconian', 'myszkowski', 'key_phrase', 'grandpre', 'columnar_transposition', 'digrafid', 'nihilist_transposition']

# fmt: on
samples = []
for file in os.listdir("data"):
    for cipher in ciphers:
        # print how many files we have for each cipher
        if cipher in file:
            samples.append(file)

print(samples)
