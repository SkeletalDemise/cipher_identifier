from statistical_tests import ioc


def get_dbic(text):
    """
    IoC of doublets
    """
    N = len(text)
    doublets = [text[index] + text[index + 1] for index in range(N - 1) if text[index] == text[index + 1]]
    return ioc.get_ioc("".join(doublets)) * 1000
