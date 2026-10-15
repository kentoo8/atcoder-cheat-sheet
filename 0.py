# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet/tree/5fe89921b13d8a8249033a8845874d1a008319d6


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
