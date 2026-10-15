import sys
from bisect import bisect_right

input = sys.stdin.readline


def read_integers() -> list[int]:
    return list(map(int, input().split()))


def read_int_matrix(n_rows: int) -> list[list[int]]:
    """整数列をn_rows行読み込み、2次元リストとして返す"""
    return [read_integers() for _ in range(n_rows)]


def get_skyline_points_from_y_x_desc(points: list[list[int]]) -> list[list[int]]:
    """
    (y, x) 降順に並んだ点 [x, y] から、
    右上から支配されない点だけを返す。

    支配の定義:
        [x1, y1] が [x2, y2] を支配する
        <=> x1 >= x2 and y1 >= y2

    返り値:
        y 昇順のまま、支配されない点だけを返す。

    計算量:
        O(N)

    イメージ:
        [y]
        ^
        | x  ●
        | x
        |   x   ●
        |  x
        |       x ●
        |
        |           x   ●
        +-----------------> [x]

        ●: 残る点
        x: 取り除かれる点
    """
    skyline: list[list[int]] = []
    max_x_seen = -(10**30)

    for x, y in points:
        if x > max_x_seen:
            skyline.append([x, y])
            max_x_seen = x
    return skyline


N = int(input())
height_leaves = read_int_matrix(N)

Q = int(input())
times = read_integers()


height_leaves.sort(key=lambda x: (x[1], x[0]), reverse=True)
skyline = get_skyline_points_from_y_x_desc(height_leaves)

leaves = [L for _, L in skyline]
heights = [H for H, _ in skyline]
leaves.reverse()
heights.reverse()

# print(leaves)
# print(heights)

ans = []
for time in times:
    idx = bisect_right(leaves, time)
    tallest_hights = heights[idx]

    ans.append(str(tallest_hights))

print("\n".join(ans))
