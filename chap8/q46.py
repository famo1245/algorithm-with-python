# BOJ 18352
import sys
from collections import deque
input = sys.stdin.readline

# N 도시의 수, M 길의 수, K 거리, X 출발 도시
N, M, K, X = map(int, input().split())
G = [[] for _ in range(N + 1)]
answer = []
visited = [-1] * (N + 1)


def bfs(v):
    que = deque()
    que.append(v)
    visited[v] += 1

    while que:
        now = que.popleft()

        for node in G[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                que.append(node)


for _ in range(M):
    S, E = map(int, input().split())
    G[S].append(E)

bfs(X)

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
