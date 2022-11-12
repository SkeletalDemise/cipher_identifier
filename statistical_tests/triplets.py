def get_triplets(text):
    """
    find number of triplets. doublet is X followed by X for any X
    """
    N = len(text)
    triplets = []
    for index in range(N - 2):
        if text[index] == text[index + 1] and text[index] == text[index + 2]:
            triplets.append(index)
    return len(triplets)
