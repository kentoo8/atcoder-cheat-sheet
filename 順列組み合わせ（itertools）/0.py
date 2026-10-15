from itertools import combinations, permutations, product

A = [1, 2, 3]

# 組合せ=combinations：順番を区別しない
# (1, 2) と (2, 1) は同じ扱い
for x in combinations(A, 2):
    print(x)
# (1, 2)
# (1, 3)
# (2, 3)


# 順列=permutations：順番を区別する
for x in permutations(A, 2):
    print(x)
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)


# 直積=product: 重複ありで全パターン
for x in product(A, repeat=2):
    print(x)
# (1, 1)
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 2)
# (2, 3)
# (3, 1)
# (3, 2)
# (3, 3)
