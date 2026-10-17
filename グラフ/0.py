def read_integers(offset=0):
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


def read_undirected_graph(
    n_vertices,
    n_edges,
    offset=0,
):
    """標準入力から、無向グラフを隣接リストとして読み込む。"""
    graph = [[] for _ in range(n_vertices)]

    for _ in range(n_edges):
        u, v = read_integers(offset)

        graph[u].append(v)
        graph[v].append(u)

    return graph


def build_dfs_tree(
    graph,
    root=0,
):
    """
    DFS木の親を返す。

    parents[v]:
        DFS木における頂点 v の親。
        根または未到達頂点では -1。
    """
    n_vertices = len(graph)

    parents = [-1] * n_vertices
    visited = [False] * n_vertices
    stack = []

    visited[root] = True
    stack.append(root)

    while stack:
        u = stack.pop()
        neighbors = graph[u]

        for v in neighbors:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                stack.append(v)

    return parents


n_vertices, n_edges = read_integers()
graph = read_undirected_graph(
    n_vertices=n_vertices,
    n_edges=n_edges,
    offset=1,
)
parents = build_dfs_tree(graph=graph)
print(graph)
print(parents)
