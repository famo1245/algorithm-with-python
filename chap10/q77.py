# BOJ 11051
# 공식
# N, K = map(int, input().split())
# divisor = 10007
#
# a = 1
# for i in range(1, N + 1):
#     a *= i % divisor
#
# b = 1
# for i in range(1, N - K + 1):
#     b *= i % divisor
#
# c = 1
# for i in range(1, K + 1):
#     c *= i % divisor
#
# print(a // (b * c) % divisor)

# 점화식
N, K = map(int, input().split())
divisor = 10007

D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 초기화
for i in range(1, N + 1):
    D[i][0] = 1
    D[i][1] = i
    if i < K + 1:
        D[i][i] = 1

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if D[i][j] == 0:
            D[i][j] = (D[i - 1][j] + D[i - 1][j - 1]) % divisor

print(D[N][K])
