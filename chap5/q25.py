import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
visit = [False] * (N+1)
near_list = [[] for _ in range(N+1)]
arrive = False


def dfs(n, d):
    global arrive
    if d == 5:
        arrive = True
        return
    else:
        visit[n] = True
        for node in near_list[n]:
            if not visit[node]:
                dfs(node, d+1)


for _ in range(M):
    u, v = map(int, input().split())
    near_list[u].append(v)
    near_list[v].append(u)

for i in range(1, N+1):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
