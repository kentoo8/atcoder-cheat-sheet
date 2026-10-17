# プリム法
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f

import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def read_integers(offset=0):
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


n_vertices, n_edges = read_integers()

# graph[v]: 頂点 v に隣接する点 u と距離 dist の組 (dist, u) のリスト
graph = [[] for _ in range(n_vertices)]

for _ in range(n_edges):
    v_i, v_j, d = read_integers()
    graph[v_i].append((d, v_j))
    graph[v_j].append((d, v_i))


# print(graph)


used_vertices = [False] * n_vertices

ans = 0
heap = []

start_vertex = 0
heap.append((0, start_vertex))  # (距離, 頂点)

while heap:
    d, v = heappop(heap)

    if used_vertices[v]:
        continue

    ans += d
    used_vertices[v] = True

    nbds = graph[v]
    for d, v in nbds:
        if not used_vertices[v]:
            heappush(heap, (d, v))

    # print()
    # print("used_vertices", used_vertices)
    # print("ans", ans)
    # print("d", d)
    # print("v", v)

print(ans)
