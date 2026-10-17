from collections import deque


def bfs_1dim():
    As = [-1, -1, 0, 0, -1, -1, -1, -1, -1, 0]
    # ほしい出力: [2, 1, 0, 0, 1, 2, 3, 2, 1, 0]

    queue = deque()

    # a == 0 である index を全て集める
    for i, a in enumerate(As):
        if a == 0:
            queue.append(i)

    while queue:
        i = queue.popleft()

        for ni in (i - 1, i + 1):
            if not 0 <= ni < len(As):
                continue

            if As[ni] != -1:
                continue

            As[ni] = As[i] + 1
            queue.append(ni)

    return As


print(bfs_1dim())
