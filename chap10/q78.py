# BOJ 2775
import sys
input = sys.stdin.readline
# 주어진 k와 n의 범위가 최대 14
MAX = 15
Apartment = [[0 for _ in range(MAX)] for _ in range(MAX)]

# DP table 초기화
for i in range(MAX):
    Apartment[0][i] = i
    # 각 층의 1호에는 1명만 있게 됨
    Apartment[i][1] = 1

# A[a][b] = A[a-1][1]+...+ A[a-1][b] = A[a][b-1] + A[a-1][b]
for i in range(1, MAX):
    for j in range(2, MAX):
        Apartment[i][j] = Apartment[i][j - 1] + Apartment[i - 1][j]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(Apartment[k][n])
