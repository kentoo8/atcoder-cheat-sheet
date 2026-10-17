# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet


def read_integers(offset=0):
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
