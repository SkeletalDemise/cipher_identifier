from statistical_tests.utils import convert_string


def get_ioc(dat):
    dat = convert_string(dat)
    cipher_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#0123456789"
    numb_symbols = len(cipher_symbols)
    ct = [0] * numb_symbols
    l = len(dat)
    for i in range(l):
        ct[dat[i]] += 1
    sum = 0.0
    for i in range(numb_symbols):
        sum += ct[i] * (ct[i] - 1)
    ic = sum / (l * (l - 1))
    return ic * 1000
