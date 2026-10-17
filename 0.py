# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet/tree/3bca2906c9e1f847e9c172b2302b775a62c5dca1


def read_integers(offset=0):
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
