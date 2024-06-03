# BOJ 11050
# 조합 공식
# N, K = map(int, input().split())
#
# a = 1
# for i in range(1, N + 1):
#     a *= i
#
# b = 1
# for i in range(1, N - K + 1):
#     b *= i
#
# c = 1
# for i in range(1, K + 1):
#     c *= i
#
# print(a // (b * c))

# 점화식
N, K = map(int, input().split())
# DP table 생성
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 초기화
for i in range(1, N + 1):
    D[i][0] = 1
    D[i][1] = i
    if i < K + 1:
        D[i][i] = 1

# D[n][k] = D[n - 1][k] + D[n - 1][k - 1]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if D[i][j] == 0:
            D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

print(D[N][K])

# N, K = map(int, input().split())
# # DP table 생성
# D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
#
# # 초기화
# for i in range(1, N + 1):
#     D[i][0] = 1
#     D[i][1] = i
#     if i < K + 1:
#         D[i][i] = 1
#
# # D[n][k] = D[n - 1][k] + D[n - 1][k - 1]
# for i in range(2, N + 1):
#     for j in range(1, i):
#         if D[i][j] == 0:
#             D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

# print(D[N][K])
# for i in D:
#     print(i)
