# 参照元（コード・スニペット）: https://github.com/kentoo8/atcoder-cheat-sheet


def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


def read_undirected_graph(
    n_vertices: int,
    n_edges: int,
    offset: int = 0,
):
    """標準入力から、無向グラフを隣接リストとして読み込む。"""
    graph = [[] for _ in range(n_vertices)]

    for idx in range(n_edges):
        u, v = read_integers(offset)

        graph[u].append((v, idx))
        graph[v].append((u, idx))

    return graph


N = int(input())
graph = read_undirected_graph(
    n_vertices=N,
    n_edges=N - 1,
    offset=1,
)


def build_euler_tour(graph, start=0):
    """根付き木のDFS行きがけ順によるオイラーツアーを非再帰で構築する。

    Args:
        graph: 無向木の隣接リスト。(隣接頂点, 辺番号) の形式。
        start: 根とする頂点番号（0-indexed）。

    Returns:
        tour: DFSの初回訪問順に並べた頂点番号。
        in_time: 各頂点の部分木の開始位置（含む）。
        out_time: 各頂点の部分木の終了位置（含まない）。
        edge_child: 各辺の根から遠い側にある頂点。

    各頂点 v の部分木は tour[in_time[v]:out_time[v]]。
    各辺 e の根から遠い側の部分木は、
    v = edge_child[e] として tour[in_time[v]:out_time[v]]。

    計算量:
        時間 O(N)、空間 O(N)。Nは頂点数。
    """
    n = len(graph)

    tour = []
    in_time = [0] * n
    out_time = [0] * n
    edge_child = [-1] * (n - 1)

    # (頂点, 親, 処理)
    stack = [(start, -1, "enter")]

    while stack:
        v, parent, action = stack.pop()

        if action == "exit":
            out_time[v] = len(tour)

        elif action == "enter":
            in_time[v] = len(tour)
            tour.append(v)

            stack.append((v, parent, "exit"))

            for w, e in reversed(graph[v]):
                if w == parent:
                    continue

                # 辺eの子側は頂点w
                edge_child[e] = w
                stack.append((w, v, "enter"))

    return tour, in_time, out_time, edge_child


tour, in_time, out_time, edge_child = build_euler_tour(graph)

for v in range(N):
    l, r = in_time[v], out_time[v]
    print()
    print(l, r)
    print(tour[l:r])
