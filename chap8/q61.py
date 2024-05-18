# BOJ 11404
import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

costs = [[math.inf] * (n + 1) for _ in range(n + 1)]

# S == E인 경우 초기화
for i in range(1, n + 1):
    costs[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b까지의 노선이 하나가 아님
    costs[a][b] = min(costs[a][b], c)

# 플로이드-워셜 알고리즘
for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            costs[s][e] = min(costs[s][e], costs[s][k] + costs[k][e])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if costs[i][j] == math.inf:
            print(0, end=' ')
        else:
            print(costs[i][j], end=' ')
    print()
