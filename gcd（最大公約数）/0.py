def gcd(a: int, b: int) -> int:
    """a, bの最大公約数"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """a, bの最小公倍数"""
    return a * b // gcd(a, b)
