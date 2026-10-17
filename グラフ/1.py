import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def read_integers():
    """整数列を1行読み込み、リストとして返す"""
    return list(map(int, input().split()))


def read_int_matrix(n_rows):
    """整数列をn_rows行読み込み、2次元リストとして返す"""
    return [read_integers() for _ in range(n_rows)]


def build_neighbors(edges):
    """
    各頂点をkey, 隣接する頂点リストをvalueに持つ辞書を返す

    例:
      [Input]
      edges = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 5]
      ]

      [Output]
      neighbors = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2],
        4: [1],
        5: [2],
      }
    """
    neighbors = defaultdict(list)

    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)

    return dict(neighbors)


def build_distances_from(
    start_vertex,
    neighbors,
):
    """
    start_vertexからの各点への距離をBFSで計算する

    例:
      [Input]
      start_vertex = 1
      neighbors = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2],
        4: [1],
        5: [2],
      }

      [Output]
      distances = {
        1: 0,
        2: 1,
        3: 1,
        4: 1,
        5: 2,
      }
    """
    distances = {start_vertex: 0}

    vertices_to_visit = deque([start_vertex])

    while vertices_to_visit:
        current_vertex = vertices_to_visit.popleft()
        neighbor_vertices = neighbors[current_vertex]

        for next_vertex in neighbor_vertices:
            # すでに距離が取得できている場合はスキップ
            if next_vertex in distances:
                continue

            distances[next_vertex] = distances[current_vertex] + 1
            vertices_to_visit.append(next_vertex)

    return distances


def find_max_distance_item(distances):
    """
    distances の中で最も距離が大きい点（のうちの1つ）とその距離の組を返す

    例:
      [Input]
      distances = {
        1: 0,
        2: 1,
        3: 1,
        4: 1,
        5: 2,
      }

      [Output]
      farthest_vertex_and_distance = (5, 2)
    """
    return max(distances.items(), key=lambda vertex_distance: vertex_distance[1])


def find_farthest_vertex_from(
    start_vertex, neighbors
):
    """
    start_vertex から最も遠い点（のうちの1つ）とその距離の組を返す

    例:
      [Input]
      start_vertex = 1
      neighbors = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2],
        4: [1],
        5: [2],
      }

      [Output]
      farthest_vertex_and_distance = (5, 2)
    """
    distances = build_distances_from(start_vertex, neighbors)
    farthest_vertex, max_distance = find_max_distance_item(distances)
    return farthest_vertex, max_distance


def find_diameter_and_endpoints(edges):
    """与えられた木(edges表示)の直径と、それを実現する端点ペアとの組を返す"""
    if len(edges) == 1:
        u, v = edges[0]
        return 1, (u, v)

    neighbors = build_neighbors(edges=edges)

    # 任意の点 start_vertex の最遠点 endpoint_1 を求め、
    # さらに endpoint_1 の最遠点 endpoint_2 を求める。このとき、
    # グラフの直径 = (endpoint_1 と endpoint_2 の距離)

    start_vertex = edges[0][0]
    endpoint_1, _ = find_farthest_vertex_from(
        start_vertex=start_vertex, neighbors=neighbors
    )

    distances_from_endpoint_1 = build_distances_from(
        start_vertex=endpoint_1, neighbors=neighbors
    )
    endpoint_2, diameter = find_max_distance_item(distances=distances_from_endpoint_1)

    return diameter, (endpoint_1, endpoint_2)


def main():
    N = int(input())
    edges = read_int_matrix(N - 1)

    diameter, _ = find_diameter_and_endpoints(edges=edges)
    print(diameter + 1)


if __name__ == "__main__":
    main()
