import itertools
from math import floor

from statistical_tests.utils import convert_string, has_digits, has_hash

# initialize AAHJU's log di table
d = "47874675736879373989676574" + "74208111630721710653712060"
d += "82527328727621822647613040"
d += "76568655843665753677656062"
d += "97888766745879775998577673"
d += "74537644722653840757624050"
d += "75547557732655752766635051"
d += "85449434831554842657625050"
d += "75877774425879764788473505"
d += "50004000300000500000600000"
d += "54327424622436531365304050"
d += "85578544825854852466655071"
d += "86438424710464761365614060"
d += "86788696846656853589656362"
d += "66776866636789772978968453"
d += "73337326721732760766603040"
d += "00000000000000000000600000"
d += "86679665836666863688656071"
d += "86768657846666874589747062"
d += "86658659833665962788747072"
d += "66766464623778560888334343"
d += "61008000700000500010210030"
d += "73347328722446730555214031"
d += "41424203510110350125202230"
d += "66666655633565863576436242"
d += "40005000300200300010200044"

logdi = [None] * 26
for i in range(26):
    logdi[i] = [0] * 26
for index, (i, j) in enumerate(itertools.product(range(26), range(26))):
    logdi[i][j] = int(d[index])


def get_rdi(num_code):
    num_code = convert_string(num_code)
    if has_digits(num_code) == "Y" or has_hash(num_code) == "Y":
        return 0
    if len(num_code) % 2 != 0:
        return 0
    l = len(num_code)
    score = 0
    ct = 0
    for i in range(0, l, 2):
        score += logdi[num_code[i + 1]][num_code[i]]
        ct += 1
    score *= 100
    score /= ct
    score = floor(score)
    return score
