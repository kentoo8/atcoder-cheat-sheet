# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet


def read_values(offset=0, type=list, cast=int):
    """空白区切りの値を1行読み込む"""
    values = (cast(x) - offset if cast is int else cast(x) for x in input().split())
    return type(values)


N, M = read_values()
