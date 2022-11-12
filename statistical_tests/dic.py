from statistical_tests.utils import convert_string


def get_dic(dat):
    dat = convert_string(dat)
    cipher_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#0123456789"
    numb_symbols = len(cipher_symbols)
    ct = [0] * numb_symbols * numb_symbols
    l = len(dat)
    for i in range(l - 1):
        ct[dat[i] + numb_symbols * dat[i + 1]] += 1
    sum = 0.0
    for i in range(numb_symbols * numb_symbols):
        sum += ct[i] * (ct[i] - 1)
    l -= 1
    ic = sum / (l * (l - 1))
    return ic * 10000
