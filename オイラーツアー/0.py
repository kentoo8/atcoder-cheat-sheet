def read_integers(offset: int = 0) -> list[int]:
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


def read_undirected_graph(
    n_vertices: int,
    n_edges: int,
    offset: int = 0,
) -> list[list[int]]:
    """標準入力から、無向グラフを隣接リストとして読み込む。"""
    graph = [[] for _ in range(n_vertices)]

    for _ in range(n_edges):
        u, v = read_integers(offset)

        graph[u].append(v)
        graph[v].append(u)

    return graph


N = int(input())
graph = read_undirected_graph(
    n_vertices=N,
    n_edges=N - 1,
    offset=1,
)


def build_euler_tour(
    graph: list[list[int]],
    start: int = 0,
):
    """根付き木のDFS行きがけ順によるオイラーツアーを非再帰で構築する。

    各頂点を初回訪問時に1回だけ記録する。
    各頂点 v の部分木は tour[in_time[v]:out_time[v]] で取得できる。

    Args:
        graph: 無向木の隣接リスト（頂点番号は0-indexed）。
        start: 根とする頂点番号。

    Returns:
        tour: DFSの初回訪問順に並べた頂点番号のリスト。
        in_time: 各頂点の部分木の開始位置（含む）。
        out_time: 各頂点の部分木の終了位置（含まない）。

    計算量:
        時間 O(N)、空間 O(N)。Nは頂点数。
    """
    n_vertices = len(graph)

    tour = []
    in_time = [0] * n_vertices
    out_time = [0] * n_vertices

    stack = [(start, -1, "enter")]  # (v, parent, action: "enter" or "exit")

    while stack:
        v, parent, action = stack.pop()

        if action == "exit":
            out_time[v] = len(tour)

        elif action == "enter":
            in_time[v] = len(tour)
            tour.append(v)

            # 子の探索が終わった後に実行したいアクション
            stack.append((v, parent, "exit"))

            for w in reversed(graph[v]):
                if w == parent:
                    continue

                stack.append((w, v, "enter"))

    return tour, in_time, out_time


tour, in_time, out_time = build_euler_tour(graph)

print()
for v in range(N):
    print(tour[in_time[v] : out_time[v]])
