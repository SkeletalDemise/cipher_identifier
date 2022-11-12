from loguru import logger


def get_binary_random(text):
    binary = "".join(format(ord(x), "b") for x in text)
    freq = binary.count("0")
    logger.trace(binary)
    return float(freq) / len(binary) * 100
