# BOJ 13251
# 공식 이용 -> 빠름
# import sys
# from math import factorial
# input = sys.stdin.readline
#
# # 각 색깔별 조약돌의 최대 개수는 50
# MAX = 51
# # 조약돌의 색상 종류수
# M = int(input())
# pebbles = list(map(int, input().split()))
# # 뽑는 조약돌의 수
# k = int(input())
#
# p = sum(pebbles)
# elementary_event = factorial(p) // (factorial(p - k) * factorial(k))
# result = 0
# for i in pebbles:
#     if i >= k:
#         result += factorial(i) // (factorial(i - k) * factorial(k))
#
# print(result / elementary_event)

import sys
input = sys.stdin.readline

# 각 색깔별 조약돌의 최대 개수는 50
MAX = 51
# 조약돌의 색상 종류수
M = int(input())
pebbles = list(map(int, input().split()))
# 뽑는 조약돌의 수
k = int(input())

# DP table
D = [[0 for _ in range(MAX * M)] for _ in range(MAX * M)]
# init DP table
for i in range(1, MAX * M):
    D[i][i] = 1
    D[i][0] = 1
    D[i][1] = i

for i in range(1, MAX * M):
    for j in range(1, i):
        if D[i][j] == 0:
            D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

elementary_event = D[sum(pebbles)][k]
events = 0
for e in pebbles:
    events += D[e][k]

print(events / elementary_event)
