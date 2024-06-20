# BOJ 1915
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
square = []

for _ in range(n):
    line = list(input().strip())
    line = list(map(int, line))
    square.append(line)

D = [[0] * m for _ in range(n)]

# init DP table
for i in range(m):
    if square[0][i] == 0:
        D[0][i] = 0
    else:
        D[0][i] = 1

# D[i][j] = min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]) + 1, in square[i][j] == 1
# D[i][j] = 0, in square[i][j] == 0
max_length = D[0][0]
for i in range(1, n):
    for j in range(m):
        if square[i][j] == 0:
            D[i][j] = 0
        else:
            D[i][j] = min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]) + 1

        if max_length < D[i][j]:
            max_length = D[i][j]

print(max_length ** 2)
