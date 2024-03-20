# BOJ 1325
# 시간 초과
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)


def bfs(v):
    que = deque()
    que.append(v)
    visited[v] = True

    while que:
        now = que.popleft()

        for i in G[now]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                que.append(i)


for _ in range(M):
    S, E = map(int, input().split())
    G[S].append(E)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    bfs(i)

maxValue = 0
for i in range(1, N + 1):
    maxValue = max(maxValue, answer[i])

for i in range(1, N + 1):
    if maxValue == answer[i]:
        print(i, end=' ')
