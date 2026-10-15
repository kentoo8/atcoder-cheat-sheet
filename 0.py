# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet/tree/e144424347a0972fa9724ce64a3c6c6ad83b35f6


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, M = read_integers()
