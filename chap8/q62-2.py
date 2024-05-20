# BOJ 11403
# using bfs
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N + 1)]
answer = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))

    for j in range(N):
        if line[j] == 1:
            G[i].append(j + 1)
            answer[i][j + 1] = 1


def bfs(s):
    visited = [False] * (N + 1)
    que = deque()
    que.append(s)

    while que:
        now = que.popleft()
        visited[now] = True

        for node in G[now]:
            answer[s][node] = 1

            if not visited[node]:
                visited[node] = True
                que.append(node)


for i in range(1, N + 1):
    bfs(i)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(answer[i][j], end=' ')
    print()
