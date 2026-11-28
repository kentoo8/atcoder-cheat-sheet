# ACL Practice J - Segment Tree
# https://atcoder.jp/contests/practice2/tasks/practice2_j
# 構築 O(N)、各クエリ O(log N)、木のメモリ O(N)

from atcoder.segtree import SegTree


def read_values(offset=0, type=list, cast=int):
    """空白区切りの値を1行読み込む"""
    values = (cast(x) - offset if cast is int else cast(x) for x in input().split())
    return type(values)


def main():
    _, q = read_values()
    values = read_values()

    # 区間同士は max で結合する。空区間の値は -1（要素はすべて非負）。
    # max_right の条件は単位元でも真である必要があり、閾値 0 でも -1 < 0。
    seg = SegTree(max, -1, values)

    for _ in range(q):
        query_type, x, y = read_values()

        if query_type == 1:
            # 1-indexed の位置 x を 0-indexed に変換して更新する。
            seg.set(x - 1, y)
        elif query_type == 2:
            # 1-indexed の閉区間 [x, y] は 0-indexed の半開区間 [x-1, y)。
            print(seg.prod(x - 1, y))
        else:
            # [x-1, r) の最大値が y 未満である最大の r を求める。
            # 右に伸ばすと最大値は下がらないので、r が最初に y 以上となる位置。
            # 見つからなければ r = N。どちらも r + 1 が出力する答え。
            r = seg.max_right(x - 1, lambda maximum: maximum < y)
            print(r + 1)


if __name__ == "__main__":
    main()
