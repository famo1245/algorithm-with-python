# BOJ 1948
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
routes = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
reversed_routes = [[] for _ in range(n + 1)]
max_time = [0] * (n + 1)

for _ in range(m):
    s, e, t = map(int, input().split())
    routes[s].append((e, t))
    degree[e] += 1
    reversed_routes[e].append((s, t))

start, end = map(int, input().split())

que = deque()
que.append(start)
while que:
    now = que.popleft()

    for t in routes[now]:
        node, value = t[0], t[1]
        max_time[node] = max(max_time[node], max_time[now] + value)
        degree[node] -= 1

        if degree[node] == 0:
            que.append(node)

print(max_time[end])

que.clear()
que.append(end)
count = 0
visited = [False] * (n + 1)
visited[end] = True
while que:
    now = que.popleft()

    for t in reversed_routes[now]:
        node, value = t[0], t[1]

        if max_time[now] == max_time[node] + value:
            count += 1

            if not visited[node]:
                visited[node] = True
                que.append(node)

print(count)

# 사용된 반례
# 5
# 7
# 1 2 1
# 1 3 3
# 2 3 2
# 2 4 1
# 2 5 3
# 3 5 1
# 4 5 1
# 1 5
# out 4 5
