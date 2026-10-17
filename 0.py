# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet/tree/0e599208d1363d66377912345d1a17933a2c860c


def read_integers(offset=0):
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
