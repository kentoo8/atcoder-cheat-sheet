# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_e
import sys

input = sys.stdin.readline


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


n_vertices, n_edges = read_integers()

# ワーシャル=フロイド法

INF = 10**19
dp = [[INF] * n_vertices for _ in range(n_vertices)]

for i in range(n_vertices):
    dp[i][i] = 0

for _ in range(n_edges):
    u, v, dist = read_integers()
    dp[u][v] = dist

for k in range(n_vertices):
    for x in range(n_vertices):
        for y in range(n_vertices):
            dp[x][y] = min(
                dp[x][y],
                dp[x][k] + dp[k][y],
            )

ans = sum(sum(xs) for xs in dp)
print(ans)
