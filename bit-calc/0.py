def on_at_k(x, k):
    """
    kビット目をオンにする
    例: 10000 | 00010 = 10010 (k=1)
    """
    return x | 1 << k


def off_at_k(x, k):
    """
    kビット目をオフにする
    例: 10111 & 11101 = 10101 (k=1)
    """
    return x & ~(1 << k)


def switch_at_k(x, k):
    """
    kビット目を反転する
    例: 10000 ^ 00010 = 10010 (k=1)
    例: 10010 ^ 00010 = 10000 (k=1)
    """
    return x ^ (1 << k)


def get_at_k(x, k):
    """kビット目を取得する"""
    if k < 0:
        return 0

    return (x >> k) & 1


def get_between_j_and_k(x, j, k):
    """j~kビット目を取得する"""
    # j <= k になるように調整
    if j > k:
        j, k = k, j

    ones = (1 << k - j) - 1  # 11...1 (k-j個の1)

    return (x >> j) & ones


x = [1, 4, 2]
x[1] = x[1] % 2
print(x)
