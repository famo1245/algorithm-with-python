# BOJ 2193
N = int(input())
D = [[0, 0] for _ in range(N + 1)]

# init DP table
D[1][1] = 1
# N == 1 인 경우
if N > 1:
    D[2][0] = 1

# D[i][0] = D[i - 1][0] + D[i - 1][1], D[i][1] = D[i - 1][0] + {D[i - 2][1]} {for i - 2 > 0}
for i in range(3, N + 1):
    D[i][0] = D[i - 1][0] + D[i - 1][1]
    D[i][1] = D[i - 1][1]
    if i - 2 > 0:
        D[i][1] += D[i - 2][1]

print(D[N][0] + D[N][1])

# N이 1일 경우 고려 할 필요 없음, 제시된 범위에서 성능차이 없음
# N = int(input())
# MAX = 90
# D = [[0, 0] for _ in range(MAX + 1)]
#
# # init DP table
# D[1][1] = 1
# D[2][0] = 1
#
# # D[i][0] = D[i - 1][0] + D[i - 1][1], D[i][1] = D[i - 1][0] + {D[i - 2][1]} {for i - 2 > 0}
# for i in range(3, MAX + 1):
#     D[i][0] = D[i - 1][0] + D[i - 1][1]
#     D[i][1] = D[i - 1][1]
#     if i - 2 > 0:
#         D[i][1] += D[i - 2][1]
#
# print(D[N][0] + D[N][1])
