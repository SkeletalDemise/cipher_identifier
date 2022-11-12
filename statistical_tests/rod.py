from statistical_tests.utils import convert_string


def get_rod(dat):
    dat = convert_string(dat)
    sum_all = sum_odd = 0
    l = len(dat)
    for i in range(l):
        for j in range(i + 1, l):
            n = 0
            while j + n < l and dat[i + n] == dat[j + n]:
                n += 1
            if n > 1:
                sum_all += 1
                if (j - i) & 1:
                    sum_odd += 1
    if sum_all == 0:
        return 50.0
    return 100.0 * sum_odd / sum_all
