import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())

near_list = [[] for _ in range(N+1)]
visit = [False] * (N+1)


def dfs(n):
    visit[n] = True
    for node in near_list[n]:
        if not visit[node]:
            dfs(node)


for _ in range(M):
    u, v = map(int, input().split())
    near_list[u].append(v)
    near_list[v].append(u)


connect = 0

for i in range(1, N+1):
    if not visit[i]:
        connect += 1
        dfs(i)

print(connect)
