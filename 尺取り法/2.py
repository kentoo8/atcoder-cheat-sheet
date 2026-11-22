# 尺取り法（Sliding Window）
# 対応問題:
# https://atcoder.jp/contests/abc032/tasks/abc032_c
# https://atcoder.jp/contests/abc485/tasks/abc485_d
#
# 共通規則:
# 1. 初期化：▲ l = 0, △ r = 0
# 2. 追加：△を1つ右へ進める
# 3. 調整：条件に従い▲を0回以上右へ進める
# 4. 記録：調整後の (l, r) から答えを更新
# 5. 終了：△が末尾に達し、最後の記録も完了
#
# 区間は常に半開区間 [l, r)
# 計算量: O(N)（状態更新・条件判定が O(1) の場合）

from collections import Counter
from collections.abc import Iterator, Sequence
from typing import Generic, TypeVar

T = TypeVar("T")


class SlidingWindow(Generic[T]):
    def __init__(self, nums: Sequence[T]):
        self.nums = nums

    def add(self, x: T) -> None:
        raise NotImplementedError

    def remove(self, x: T) -> None:
        raise NotImplementedError

    def should_shrink(self) -> bool:
        raise NotImplementedError

    def scan(self) -> Iterator[tuple[int, int]]:
        l = 0

        for r, x in enumerate(self.nums):
            # 2. △を進める
            self.add(x)

            # 3. ▲を調整する
            while self.should_shrink():
                self.remove(self.nums[l])
                l += 1

            # 4. 記録用に [l, r) を渡す
            yield l, r + 1


# ─────────────────────────────────────
# ABC032 C：積が K 以下の連続部分列の最大長
# ─────────────────────────────────────


class ProductWindow(SlidingWindow[int]):
    def __init__(self, nums: Sequence[int], k: int):
        super().__init__(nums)
        self.k = k
        self.prd = 1

    def add(self, x: int) -> None:
        self.prd *= x

    def remove(self, x: int) -> None:
        self.prd //= x

    def should_shrink(self) -> bool:
        return self.prd > self.k


def solve_abc032_c(nums: list[int], k: int) -> int:
    n = len(nums)

    if 0 in nums:
        return n
    if k == 0:
        return 0

    ans = 0
    for l, r in ProductWindow(nums, k).scan():
        ans = max(ans, r - l)

    return ans


# ─────────────────────────────────────
# ABC485 D：ABC | ABC | ABC
# ─────────────────────────────────────


class ABCWindow(SlidingWindow[str]):
    def __init__(self, s: str):
        super().__init__(s)
        self.cnt = Counter()

    def add(self, x: str) -> None:
        self.cnt[x] += 1

    def remove(self, x: str) -> None:
        self.cnt[x] -= 1

    def should_shrink(self) -> bool:
        return all(self.cnt[x] > 0 for x in "ABC")


def solve_abc485_d(s: str) -> int:
    if not all(x in s for x in "ABC"):
        return 0

    n = len(s)

    # 左右の部分文字列にABCを残す
    left = max(s.index(x) for x in "ABC") + 1
    right = n - 1 - max(s[::-1].index(x) for x in "ABC")

    middle = s[left:right]

    ans = 0
    for l, r in ABCWindow(middle).scan():
        ans += l

    return ans


# ─────────────────────────────────────
# 使用例（ローカル確認用）
# ─────────────────────────────────────

if __name__ == "__main__":
    # ABC032 C
    assert solve_abc032_c([8, 2, 3], 6) == 2
    assert solve_abc032_c([5, 5], 3) == 0
    assert solve_abc032_c([0, 5], 0) == 2

    # ABC485 D
    assert solve_abc485_d("AABCCABCCBCA") == 5
