def get_doublets(text):
    """
    find number of doublets. doublet is X followed by X for any X
    """
    N = len(text)
    doublets = [index for index in range(N - 1) if text[index] == text[index + 1]]
    return len(doublets)
