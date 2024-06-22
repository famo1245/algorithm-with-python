# BOJ 1328
import sys
from math import factorial

input = sys.stdin.readline
N, L, R = map(int, input().split())
DIVISOR = 1000000007
MAX = 100
# D[N][L][R] => 건물이 N개 일 때, R과 L에서 가능한 경우의 수
D = [[[0] * (n + 1) for _ in range(n + 1)] for n in range(MAX + 1)]

# init DP table
# N이 1일 때 건물 1개로 좌, 우 어디든 1개
D[1][1][1] = 1
# N이 2일 때 L,R이 2, 1이거나 1, 2인 경우에만 가능 => 건물의 높이는 모두 다르기 떄문
D[2][2][1] = 1
D[2][1][2] = 1

for n in range(3, N + 1):
    # L = 1, R = 1은 N이 2 이상 부터 불가능
    for l in range(1, n + 1):
        for r in range(1, l + 1):
            # 좌 우에서 본 건물 수의 합이 전체 건물 수 + 2 이상 배치 불가능
            if l + r < n + 2:
                # if l == r:
                #     D[n][l][r] = (D[n - 1][l - 1][r] + D[n - 1][l][r - 1]) % DIVISOR
                # else:
                #     D[n][l][r] = (D[n - 1][l - 1][r - 1] * factorial(n - 2)) % DIVISOR
                result = 0
                for i in range(l + 1):
                    for j in range(r + 1):
                        if i < n and j < n:
                            result += D[n - 1][i][j]
                D[n][l][r] = result
                # 좌우 건물의 수를 뒤집었을 때 같은 경우의 수가 나옴
                D[n][r][l] = D[n][l][r]

# for i in range(1, N + 1):
#     print("n:", i)
#     for j in range(len(D[i])):
#         print(D[i][j])
print(D[N][L][R] % DIVISOR)
