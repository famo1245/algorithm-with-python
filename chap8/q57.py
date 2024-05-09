# BOJ 1916
import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [False] * (n + 1)
routes = [[] for _ in range(n + 1)]
costs = [math.inf] * (n + 1)

for _ in range(m):
    s, e, v = map(int, input().split())
    routes[s].append((e, v))

start, end = map(int, input().split())
costs[start] = 0
que = PriorityQueue()
que.put((costs[start], start))

while not que.empty():
    now = que.get()[1]

    if visited[now]:
        continue

    visited[now] = True

    for t in routes[now]:
        node, value = t[0], t[1]

        if costs[node] > costs[now] + value:
            costs[node] = costs[now] + value
            que.put((costs[node], node))

print(costs[end])
