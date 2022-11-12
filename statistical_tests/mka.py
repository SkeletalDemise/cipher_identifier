from statistical_tests.utils import convert_string


def get_kappa(text):
    text = convert_string(text)
    max_period = 15
    mx = 0.0
    for period in range(1, max_period):
        if period >= len(text):
            break
        ct = 0.0
        for i in range(len(text) - period):
            if text[i] == text[i + period]:
                ct += 1.0
        z = ct / (len(text) - period)
        if z > mx:
            mx = z
    return 1000.0 * mx
