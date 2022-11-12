def get_quadruplets(text):
    """
    find number of quadruplets. doublet is X followed by X for any X
    """
    N = len(text)
    quadruplets = []
    for index in range(0, N - 3):
        if (text[index] == text[index + 1] and text[index] == text[index + 2] and text[index] == text[index + 3]):
            quadruplets.append(index)
    return len(quadruplets)
