def inverse(P: list[int], start=0) -> list[int]:
    """順列の逆元を返す"""
    P = [x - start for x in P]  # 0-index化

    invP = [0] * len(P)

    for i in range(len(P)):
        invP[P[i]] = i

    invP = [x + start for x in invP]  # 元のindexに戻す
    return invP


def swap(P: list, i: int, j: int, start=0) -> None:
    """位置i, jの要素を入れ替える"""
    i -= start
    j -= start
    P[i], P[j] = P[j], P[i]


P = [1, 4, 2, 3]
invP = inverse(P, start=1)

print(P)
print(invP)
print(swap(P, 1, 2, start=1))
