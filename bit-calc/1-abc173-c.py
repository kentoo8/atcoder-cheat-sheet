import sys

input = sys.stdin.readline


def read_values(offset=0, type=list, cast=int):
    """空白区切りの値を1行読み込む"""
    values = (cast(x) - offset if cast is int else cast(x) for x in input().split())
    return type(values)


def read_board(height):
    """
    height 行の文字列を読み込み、2次元リストとして返す。

    例:
        入力:
            .#.
            ##.

        戻り値:
            [
                [".", "#", "."],
                ["#", "#", "."],
            ]
    """
    return [list(input().strip()) for _ in range(height)]


H, W, K = read_values()
board = read_board(H)

ans = 0
for bit_y in range(1 << H):
    for bit_x in range(1 << W):
        cnt = 0
        for i in range(H):
            if bit_y >> i & 1:
                for j in range(W):
                    if bit_x >> j & 1:  # noqa: SIM102
                        if board[i][j] == "#":
                            cnt += 1
        if cnt == K:
            ans += 1

print(ans)
