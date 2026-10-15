S = input().strip()
T = input().strip()

H = len(S)
W = len(T)

# dp[i][j]: S[:i] と T[:j] の最長共通部分列の長さ
dp = [[0] * (W + 1) for _ in range(H + 1)]

# どこから来たか
LU = 0
L = 1
U = 2
parent = [[-1] * (W + 1) for _ in range(H + 1)]

for i in range(H):
    for j in range(W):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
            parent[i + 1][j + 1] = LU

        elif dp[i + 1][j] >= dp[i][j + 1]:
            dp[i + 1][j + 1] = dp[i + 1][j]
            parent[i + 1][j + 1] = L

        else:  # dp[i + 1][j] < dp[i][j + 1]
            dp[i + 1][j + 1] = dp[i][j + 1]
            parent[i + 1][j + 1] = U


ans_reverse = ""

i = H
j = W

while i >= 0 and j >= 0:
    # print("i,j", i, j)

    if parent[i][j] == LU:
        ans_reverse += S[i - 1]
        i -= 1
        j -= 1

    elif parent[i][j] == L:
        j -= 1

    else:  # parent[i][j] == U
        i -= 1

ans = ans_reverse[::-1]
print(ans)
