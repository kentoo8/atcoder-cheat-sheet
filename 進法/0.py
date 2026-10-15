def int_to_adic(n: int, p: int):
    """正の整数 n をp進法のリストに変換する"""
    out = []
    while n:
        n, m = divmod(n, p)
        out.append(m)

    out.reverse()

    return out


def adic_to_int(x: list[int], p: int) -> int:
    """p進法のリストを整数に変換する"""
    return sum(xi * p**k for k, xi in enumerate(reversed(x)))
