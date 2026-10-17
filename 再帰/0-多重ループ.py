S = "ab"


def rec3():
    ans = []
    for s1 in S:
        for s2 in S:
            for s3 in S:
                ans.append(s1 + s2 + s3)

    return ans


print(rec3())


def rec3_():
    path0 = ""
    ans = []

    for s1 in S:
        path1 = path0 + s1

        for s2 in S:
            path2 = path1 + s2

            for s3 in S:
                path3 = path2 + s3
                ans.append(path3)

    return ans


print(rec3_())


def rec3__(path=""):
    """rec3_を再帰化"""
    if len(path) == 3:
        return [path]

    ans = []

    for s in S:
        new_path = path + s
        new_ans = rec3__(new_path)
        ans.extend(new_ans)

    return ans


print(rec3__())


def rec(path="", length=3):
    """探索木の深さを変数化"""
    if len(path) == length:
        return [path]

    ans = []

    for s in S:
        new_path = path + s
        new_ans = rec(new_path, length)
        ans.extend(new_ans)

    return ans


print(rec())
