# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet/tree/281462264e7f2969b3e0fc159145029b9ea50c9c


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
