def convert_string(code):
    cipher_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#0123456789"
    num_code = []
    code = code.upper()
    code = code.replace("Ø", "0")
    clen = 0
    for i in range(len(code)):
        n = cipher_symbols.index(code[i]) if code[i] in cipher_symbols else -1
        if n != -1:
            num_code.append(n)
            clen += 1
    return num_code


def has_digits(dat):
    l1 = "N"
    for i in range(len(dat)):
        c = dat[i]
        if c > 26:
            l1 = "Y"
    return l1


def has_hash(dat):
    l4 = "N"
    for i in range(len(dat)):
        c = dat[i]
        if c == 26:
            l4 = "Y"
    return l4
