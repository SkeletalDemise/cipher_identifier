import itertools
from statistical_tests.utils import convert_string


def get_max_periodic_ic(text):
    text = convert_string(text)
    max_period = 15
    cipher_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#0123456789"
    numb_symbols = len(cipher_symbols)
    i = 0
    j = 0
    l = 0
    mx = 0.0
    period = 0
    index = 0
    x = 0.0
    y = 0.0
    z = 0.0
    mx = 0.0

    l = len(text)
    ct = [[0] * numb_symbols for _ in range(max_period + 1)]
    for period in range(1, max_period + 1):
        for i, j in itertools.product(range(period), range(numb_symbols)):
            ct[i][j] = 0
        index = 0
        for i in range(l):
            ct[index][text[i]] += 1
            index = (index + 1) % period
        z = 0.0
        for i in range(period):
            x = y = 0.0
            for j in range(numb_symbols):
                x += ct[i][j] * (ct[i][j] - 1)
                y += ct[i][j]
            if y > 1:
                z += x / (y * (y - 1))
        z = z / period
        if z > mx:
            mx = z
    return 1000.0 * mx
