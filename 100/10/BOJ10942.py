# BOJ 10942
import sys
input = sys.stdin.readline

N = int(input())
nums = [-1] + input().split()
D = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    D[i][i] = 1

for i in range(1, N):
    if nums[i] == nums[i + 1]:
        D[i][i + 1] = 1

for length in range(3, N + 1):
    for start in range(1, N - length + 2):
        end = start + length - 1
        if nums[start] == nums[end] and D[start + 1][end - 1]:
            D[start][end] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(D[S][E])

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# nums = [-1] + list(map(int, input().split()))
# D = [[0] * (N + 1) for _ in range(N + 1)]
#
# for i in range(2, N):
#     j = 1
#     while i - j > 0 and i + j <= N:
#         if nums[i - j] == nums[i + j]:
#             D[i - j][i + j] = 1
#         else:
#             break
#         j += 1
#
# for i in range(2, N):
#     if nums[i] != nums[i + 1]:
#         continue
#     j = 1
#     while i - j > 0 and i + 1 + j <= N:
#         if nums[i - j] == nums[i + 1 + j]:
#             D[i - j][i + 1 + j] = 1
#         else:
#             break
#         j += 1
#
# M = int(input())
# for _ in range(M):
#     st, ed = map(int, input().split())
#     if ed - st == 1:
#         print(1 if nums[st] == nums[ed] else 0)
#     elif ed - st == 0:
#         print(1)
#     else:
#         print(D[st][ed])
