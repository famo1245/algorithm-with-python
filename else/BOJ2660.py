# BOJ 2660
import sys
from math import inf
input = sys.stdin.readline

N = int(input())
relationship = [[inf] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    relationship[i][i] = 0

a, b = 0, 0
while a + b != -2:
    a, b = map(int, input().split())
    relationship[a][b] = 1
    relationship[b][a] = 1

for k in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            relationship[s][e] = min(relationship[s][e], relationship[s][k] + relationship[k][e])

min_point = inf
min_list = []
for i in range(1, N + 1):
    point = max(relationship[i][1:N+1])

    if min_point > point:
        min_point = point
        min_list = [i]
    elif min_point == point:
        min_list.append(i)

min_list.sort()
print(min_point, len(min_list))
print(*min_list)
