# クラスカル法
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f

import sys

input = sys.stdin.readline


def read_integers(offset=0):
    """整数列を1行読み込む"""
    return [x - offset for x in map(int, input().split())]


class UnionFind:
    def __init__(self, n):
        """n 個の要素を、それぞれ別の集合として初期化する"""
        self._parent = [-1] * n
        self._size = [1] * n  # 根に対してのみ、正しい集合サイズを保持する

    def find_root(self, v):
        """v が属する集合の代表元を返す"""
        path = []
        while self._parent[v] != -1:
            path.append(v)
            v = self._parent[v]
        root = v

        # 経路圧縮（pathの元を、すべて根の子に繋ぎ直す）
        for v in path:
            self._parent[v] = root

        return root

    def unite(self, u, v):
        """
        u と v の属する集合を併合して True を返す。
        ただし、すでに同じ集合なら何もせず False を返す。
        """
        root_of_u = self.find_root(u)
        root_of_v = self.find_root(v)

        if root_of_u != root_of_v:
            # 必ず root_of_u: サイズが小さい側, root_of_v: 大きい側 になるようにする
            if self._size[root_of_u] > self._size[root_of_v]:
                root_of_u, root_of_v = root_of_v, root_of_u

            # union-by-size: サイズが小さい集合から大きい集合へ向けて辺を張る
            self._parent[root_of_u] = root_of_v
            self._size[root_of_v] += self._size[root_of_u]

            return True
        else:
            return False

    def in_same_set(self, u, v):
        """u と v が同じ集合に属するかを返す"""
        return self.find_root(u) == self.find_root(v)

    def size(self, v):
        """v が属する集合の要素数を返す"""
        root = self.find_root(v)
        return self._size[root]


n_vertices, n_edges = read_integers()

edges = []
for _ in range(n_edges):
    u, v, dist = read_integers()
    edges.append([dist, u, v])

edges.sort()
# print(edges)


uf = UnionFind(n=n_vertices)

total_dist = 0
for dist, u, v in edges:
    if uf.unite(u, v):
        total_dist += dist


print(total_dist)
