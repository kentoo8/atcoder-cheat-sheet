# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet/tree/64cc7805b99401d97af6537efd1b5fdcad029d39


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
