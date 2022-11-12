from statistical_tests.utils import convert_string, has_digits, has_hash


def get_normor(num_code):
    num_code = convert_string(num_code)
    if has_digits(num_code) == "Y" or has_hash(num_code) == "Y":
        return 0

    english_freq_list = [
        4,
        19,
        0,
        14,
        8,
        13,
        18,
        17,
        7,
        11,
        3,
        20,
        2,
        12,
        6,
        5,
        24,
        15,
        22,
        1,
        21,
        10,
        23,
        9,
        25,
        16,
    ]

    # get letter frequencies in the code
    freq = []
    for i in range(26):
        freq.append(0)
    for i in range(len(num_code)):
        n = num_code[i]
        if n < 26:
            freq[n] += 1

    # get list of the unique letter frequencies
    vals = []
    for i in range(26):
        n = freq[i]
        if n not in vals:
            vals.append(n)

    vals.sort(reverse=True)  # descending numerical sort
    # make list of the code letters in order of their frequencies, highest first, equal frequencies in
    # alphabetical order
    freq_order = []
    for i in range(len(vals)):
        n = vals[i]
        for j in range(26):
            if freq[j] == n:
                freq_order.append(j)

    # sum the differences in position between each letter in the code frequencies and in standard
    # english frequencies
    letter_sum = 0
    for i in range(26):
        n = english_freq_list.index(i) - freq_order.index(i)
        if n < 0:
            n = -n
        letter_sum += n

    return letter_sum
