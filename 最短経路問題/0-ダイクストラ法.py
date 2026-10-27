# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def read_integers(offset=0):
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


def dijkstra(graph, start_vertex, goal_vertex):
    """
    ダイクストラ法を用いて、始点から終点までの最短距離を求める。

    Args:
        graph: 隣接リスト。graph[u] は頂点uから出る辺の
            (距離 dist, 行き先 v) のリスト。頂点番号は 0, 1, ..., len(graph) - 1.
        start_vertex: 始点の頂点番号。
        goal_vertex: 終点の頂点番号。

    Returns:
        始点から終点までの最短距離。到達不能の場合は-1。

    計算量: O(V + E log(E + 1))。Vは頂点数、Eは辺数。
    注: グラフの辺の重みは非負であることが必要。
    注: グラフの辺の重みが全て同じ場合は、BFS を用いると計算量 O(V + E) で求められる。
    """
    n_vertices = len(graph)

    heap = []
    heappush(heap, (0, start_vertex))

    INF = float("inf")
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

    ans = dists[goal_vertex]
    return ans if ans < INF else -1


n_vertices, n_edges = read_integers()

graph = [[] for _ in range(n_vertices)]

for _ in range(n_edges):
    u, v, dist = read_integers()
    graph[u].append((dist, v))


start = 0
goal = n_vertices - 1
ans = dijkstra(graph, start, goal)

print(ans)
