from statistical_tests.utils import convert_string


def get_even_dic(text):
    text = convert_string(text)
    cipher_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#0123456789"
    numb_symbols = len(cipher_symbols)
    ct = [0] * numb_symbols * numb_symbols
    l = len(text)
    n = 0
    for i in range(0, l - 1, 2):
        ct[text[i] + numb_symbols * text[i + 1]] += 1
        n += 1
    sum = 0.0
    for i in range(numb_symbols * numb_symbols):
        sum += ct[i] * (ct[i] - 1)
    ic = sum / (n * (n - 1))
    return ic * 10000
