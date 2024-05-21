# BOJ 1389
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
relationship = [[math.inf] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    relationship[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    relationship[a][b] = 1
    relationship[b][a] = 1

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            relationship[s][e] = min(relationship[s][e], relationship[s][k] + relationship[k][e])

# kevin_nums = []
# for i in range(1, n + 1):
#     kevin_num = 0
#     for j in range(1, n + 1):
#         kevin_num += relationship[i][j]
#
#     kevin_nums.append((kevin_num, i))
#
# print(min(kevin_nums)[1])

min_kevin_num = math.inf
person_num = -1
for i in range(1, n + 1):
    kevin_num = 0
    for j in range(1, n + 1):
        kevin_num += relationship[i][j]

    if min_kevin_num > kevin_num:
        min_kevin_num = kevin_num
        person_num = i

print(person_num)
