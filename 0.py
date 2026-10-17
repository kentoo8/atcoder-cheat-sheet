# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet/tree/d698f21df64c005830a67edb842129fa4725e153


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
