import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, start = map(int, input().split())
near_list = [[] for _ in range(N+1)]
visit = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    near_list[u].append(v)
    near_list[v].append(u)

for l in near_list:
    l.sort()


def dfs(n):
    print(n, end=' ')
    visit[n] = True

    for node in near_list[n]:
        if not visit[node]:
            dfs(node)


dfs(start)
print()
visit = [False] * (N + 1)


def bfs(n):
    queue = deque()
    queue.append(n)
    visit[n] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for node in near_list[now]:
            if not visit[node]:
                visit[node] = True
                queue.append(node)


bfs(start)
