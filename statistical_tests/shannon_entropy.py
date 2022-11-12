import math
from collections import Counter


def get_shannon_entropy(text):
    """
    O(n) algorithm to calculate the shannon entropy of the text
    """
    text_length = float(len(text))
    return -sum(
        map(
            lambda a: (a / text_length) * math.log2(a / text_length),
            Counter(text).values(),
        )
    )
