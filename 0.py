# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet/tree/7e82ad0e8d4e4859b0e5d4549f1990c9950531a3


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
