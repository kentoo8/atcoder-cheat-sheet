from bisect import bisect_left, bisect_right

x = list(map(int, input().split()))  # 11 22 33 44 55 66 77 88 99

print(bisect_left(x, 33))  # 2
print(bisect_right(x, 33))  # 3

print()

print(bisect_left(x, 30))  # 2
print(bisect_right(x, 30))  # 2


idx = bisect_right(x, 33)
print(x[:idx])  # [11, 22, 33]
print(x[idx:])  # [44, 55, 66, 77, 88, 99]
