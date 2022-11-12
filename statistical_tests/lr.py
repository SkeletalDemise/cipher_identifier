from math import sqrt
from statistical_tests.utils import convert_string


def get_lr(dat):
    dat = convert_string(dat)
    reps = [0] * 11
    l = len(dat)
    for i in range(l):
        for j in range(i + 1, l):
            n = 0
            while j + n < l and dat[i + n] == dat[j + n]:
                n += 1
            if n > 10:
                n = 10
            reps[n] += 1
    return 1000.0 * sqrt(reps[3]) / l
