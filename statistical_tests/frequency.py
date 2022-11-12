def get_frequency(text, n):
    n = n or 1
    n = int(n)
    text = text.upper()

    freq = {}
    for i in range(len(text) - n):
        character = text[i]
        for j in range(1, n):
            character += text[i + j]
        if character in freq:
            freq[character] += 1
        else:
            freq[character] = 1

    return freq
