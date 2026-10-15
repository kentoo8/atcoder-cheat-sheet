# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
import sys

input = sys.stdin.readline


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


n_vertices, n_edges = read_integers()

# ダイクストラ法
# graph[u]: uから出る辺の (距離 dist, 行き先 u) のリスト
graph = [[] for _ in range(n_vertices)]

for _ in range(n_edges):
    u, v, dist = read_integers()
    graph[u].append((dist, v))

from heapq import heappop, heappush

start_vertex = 0

heap = []
heappush(heap, (0, start_vertex))

INF = 10**19
dists = [INF] * n_vertices
dists[start_vertex] = 0

while heap:
    dist, v = heappop(heap)
    nbds = graph[v]

    # すでにもっと短い経路が見つかっているなら、
    # このヒープ要素は古いので捨てる
    if dist > dists[v]:
        continue

    for next_dist, next_v in nbds:
        if dists[next_v] > dist + next_dist:
            dists[next_v] = dist + next_dist
            heappush(heap, (dist + next_dist, next_v))

# print(dists)

ans = dists[n_vertices - 1]
print(ans)
