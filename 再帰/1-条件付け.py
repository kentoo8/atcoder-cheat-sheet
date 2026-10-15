S = "abc"


def rec(n: int, path="") -> list[str]:
    """pathに残りn文字を加えてできる全ての文字列のリストを返す"""
    if n == 0:
        return [path]

    ans = []
    for s in S:
        new_path = path + s
        new_ans = rec(n - 1, new_path)
        ans.extend(new_ans)

    return ans


print(rec(n=3))


def rec1(n: int, path="") -> list[str]:
    """pathに残りn文字を加えてできる文字列で、隣り合う文字が異なるもの全体のリストを返す"""
    if n == 0:
        return [path]

    ans = []
    for s in S:
        if not path or (path[-1] != s):
            new_path = path + s
            new_ans = rec1(n - 1, new_path)
            ans.extend(new_ans)

    return ans


print(rec1(n=5))
