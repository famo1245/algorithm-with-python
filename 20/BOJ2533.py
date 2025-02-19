# BOJ 2533
import sys
input = sys.stdin.readline

N = int(input())
T = [[] for _ in range(N + 1)]
D = [[0, 0] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    T[u].append(v)
    T[v].append(u)

stack = [(1, -1, 0)]
visited = [False] * (N + 1)
finished = [False] * (N + 1)

while stack:
    now, parent, state = stack[-1]

    if state == 0:
        visited[now] = True
        stack[-1] = (now, parent, 1)

        for child in T[now]:
            if child != parent and not visited[child]:
                stack.append((child, now, 0))

    else:
        stack.pop()
        if finished[now]:
            continue

        D[now][0] = 0
        D[now][1] = 1

        for child in T[now]:
            if child != parent:
                D[now][1] += min(D[child][0], D[child][1])
                D[now][0] += D[child][1]

        finished[now] = True

print(min(D[1][0], D[1][1]))
