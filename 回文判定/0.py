def is_palindromic(xs: list | str) -> bool:
    """回文判定"""
    n = len(xs)

    return all(xs[i] == xs[n - i - 1] for i in range(n // 2))
