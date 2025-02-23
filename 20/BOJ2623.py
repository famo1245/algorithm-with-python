# BOJ 2623
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0] * (N + 1)
degree[0] = -1
G = [[] for _ in range(N + 1)]

for _ in range(M):
    order = list(map(int, input().split()))

    for i in range(1, len(order) - 1):
        prev, next = order[i], order[i + 1]
        G[prev].append(next)
        degree[next] += 1

q = deque()
for i in range(N + 1):
    if degree[i] == 0:
        q.append(i)

count = N
answer = []
while q:
    now = q.popleft()
    count -= 1
    answer.append(now)

    for next in G[now]:
        degree[next] -= 1

        if degree[next] == 0:
            q.append(next)

if count:
    print(0)
else:
    for i in answer:
        print(i)
