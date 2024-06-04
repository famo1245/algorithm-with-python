# BOJ 1010
import sys
input = sys.stdin.readline
# N, M의 최댓값
MAX = 31
D = [[0 for _ in range(MAX)] for _ in range(MAX)]

# DP table 초기화
for i in range(MAX):
    D[i][0] = 1
    D[i][i] = 1
    D[i][1] = i

for i in range(1, MAX):
    for j in range(1, i):
        if D[i][j] == 0:
            D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(D[M][N])
