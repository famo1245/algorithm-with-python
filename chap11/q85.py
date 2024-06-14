# BOJ 14501
# 무조건 상담이 끝난 날 상담을 바로 할 필요x
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# schedule = [0] * (N + 1)
# D = [0] * (N + 1)
#
# for i in range(1, N + 1):
#     t, p = map(int, input().split())
#     schedule[i] = (t, p)
#
# for i in range(1, N + 1):
#     date = i
#     profit = 0
#     while date < N + 1:
#         t, p = schedule[date]
#         # 상담 기간이 퇴사일 이후일 때
#         if date + t > N + 1:
#             break
#         profit += p
#         date += t
#
#     D[i] = profit
# print(max(D))

import sys

input = sys.stdin.readline
N = int(input())
schedule = [0] * (N + 1)
profit = [0] * (N + 1)
D = [0] * (N + 2)

for i in range(1, N + 1):
    t, p = map(int, input().split())
    schedule[i] = t
    profit[i] = p

# init DP table
D[N + 1] = 0
if schedule[N] > 1:
    D[N] = 0
else:
    D[N] = profit[N]

# D[i] = D[i + 1] or D[i] = max(D[i + 1], D[i + t] + p)
for i in range(N - 1, 0, -1):
    if schedule[i] + i > N + 1:
        D[i] = D[i + 1]
    else:
        D[i] = max(D[i + 1], D[i + schedule[i]] + profit[i])

print(max(D))
