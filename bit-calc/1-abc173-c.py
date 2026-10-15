import sys

input = sys.stdin.readline


def read_integers() -> list[int]:
    """
    1行の整数列を読み込み、リストとして返す。

    例:
        入力: 3 5 7
        戻り値: [3, 5, 7]
    """
    return list(map(int, input().split()))


def read_board(height: int) -> list[list[str]]:
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


H, W, K = read_integers()
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
