# https://atcoder.jp/contests/abc032/tasks/abc032_c
# 問題: 非負整数列 nums の連続部分列で積が K 以下のもののうち、長さが一番長いものの長さを求めよ.
# 解法: 尺取り法
# 計算速度: O(N)


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


N, K = read_integers()
nums = [int(input()) for _ in range(N)]


def main():
    if 0 in nums:
        return N

    if K == 0:
        return 0

    # 尺取り法
    l = 0
    r = 0

    prd = 1
    ans = 0

    while r < N:
        prd *= nums[r]
        r += 1

        while prd > K:
            prd //= nums[l]
            l += 1

        ans = max(ans, r - l)

    return ans


print(main())
