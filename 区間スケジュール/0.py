def is_overlapped(
    l0: int,
    r0: int,
    l1: int,
    r1: int,
    strict=False,
) -> bool:
    """区間[l0,r0]と[l1,r1]が重なっているか？"""
    if strict:
        return l0 < r1 and l1 < r0
    return l0 <= r1 and l1 <= r0


# 区間版
def is_overlapped_(
    A: list[int],
    B: list[int],
    strict=False,
) -> bool:
    """区間AとBが重なっているか？"""
    if strict:
        return A[0] < B[1] and A[1] < B[0]
    return A[0] <= B[1] and A[1] <= B[0]
