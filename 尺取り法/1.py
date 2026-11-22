# https://atcoder.jp/contests/abc485/tasks/abc485_d
# ABC | ABC | ABC

from collections import Counter

ABC = "ABC"

N = int(input())
S = list(input().strip())
S_reversed = list(reversed(S))


def _contains_ABC(cnt):
    return all(cnt[x] >= 1 for x in "ABC")


def main():
    if not _contains_ABC(Counter(S)):
        return 0

    l_ = max(S.index(x) for x in "ABC") + 1
    r_ = N - max(S_reversed.index(x) for x in "ABC") - 1

    S_ = S[l_:r_]
    M = len(S_)

    cnt = Counter()
    ans = 0

    r = 0
    for l in range(M):
        while r < M:
            if _contains_ABC(cnt):
                break

            cnt[S_[r]] += 1
            r += 1

        if not _contains_ABC(cnt):
            break

        ans += M - r + 1
        cnt[S_[l]] -= 1

    return ans


print(main())
