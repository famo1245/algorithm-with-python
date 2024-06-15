# BOJ 11726
# MAX = 1000
# DIVISOR = 10007
# N = int(input())
# # D[n][0] => 세로, D[n][1] => 가로, D[n][2] => mix
# D = [[0, 0, 0] for _ in range(MAX + 1)]
#
# # init DP table
# D[1][0] = 1
# D[2][0] = 1
# D[2][1] = 1
#
# for i in range(3, MAX + 1):
#     D[i][0] = D[i - 1][0]
#     D[i][1] = D[i // 2][1]
#     if i % 2 == 0:
#         D[i][2] = (D[i - 1][2] + D[i // 2][1]) % DIVISOR
#     else:
#         D[i][2] = (D[i - 1][1] + D[i - 1][2]) * 2 % DIVISOR
#
# print(D[N])
# print(sum(D[N]))

# D[i] = D[i - 2] + D[i - 1]
MAX = 1000
DIVISOR = 10007
N = int(input())
D = [0] * (MAX + 1)

# init DP table
D[1] = 1
D[2] = 2

for i in range(3, MAX + 1):
    D[i] = (D[i - 2] + D[i - 1]) % DIVISOR

print(D[N])
