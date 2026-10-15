import sys

input = sys.stdin.readline


def read_integers() -> list[int]:
    """整数列を1行読み込み、リストとして返す"""
    return list(map(int, input().split()))


def read_int_matrix(n_rows: int) -> list[list[int]]:
    """整数列をn_rows行読み込み、2次元リストとして返す"""
    return [read_integers() for _ in range(n_rows)]


def get_skyline_points_from_y_desc(points) -> list[list[int]]:
    """
    y 降順に並んだ点 [x, y] から、右上から支配されない点だけを返す。

    順序:
        [x1, y1] <= [x2, y2]
        :<=> x1 <= x2 and y1 <= y2

    計算量:
        O(N)

    イメージ:
        y
        ^
        | x  ●
        | x
        |   x   ●
        |  x
        |       x ●
        |
        |           x   ●
        +-----------------> x

        ●: 残る点
        x: 取り除かれる点
    """
    skyline = []
    max_x_seen = -(10**30)

    for x, y in points:
        # 前提から、y 降順で取り出されるので、
        # すでに見た点は、全て現在の点以上の y を持つ。
        #
        # もし x <= max_x_seen なら、
        # 「x も y も現在以上」の既出点があるので、
        # 現在の点 [x, y] は支配されている。
        #
        # ゆえにskylineに採用しない。
        if x <= max_x_seen:
            continue

        # max_x_seen < x 、つまり x が過去最大を更新するなら、
        # 現在の点を支配する既出点は存在しない。
        #
        # ゆえにskylineに採用する。
        skyline.append([x, y])
        max_x_seen = x

    return skyline


def get_skyline_points_from_y_asc(points: list[list[int]]) -> list[list[int]]:
    """
    y 昇順に並んだ点 [x, y] から、右上から支配されない点だけを返す。

    計算量:
        O(N)
    """
    skyline = get_skyline_points_from_y_desc(reversed(points))
    skyline.reverse()
    return skyline


# --


n = 5
points = [(1, 8), (2, 8), (3, 5), (2, 4), (1, 3), (3, 3)]


skyline = get_skyline_points_from_y_desc(points)
print(skyline)
