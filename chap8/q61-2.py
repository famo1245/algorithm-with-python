# BOJ 11404
# using bfs -> Time out
# import sys
# from collections import deque
# import math
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
#
# costs = [[math.inf] * (n + 1) for _ in range(n + 1)]
# routes = [[] for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     costs[i][i] = 0
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     routes[a].append(b)
#     costs[a][b] = min(costs[a][b], c)
#
#
# def modified_bfs(s):
#     visited = [False] * (n + 1)
#     que = deque()
#     que.append(s)
#
#     while que:
#         now = que.popleft()
#         visited[now] = True
#
#         for node in routes[now]:
#             if costs[s][node] > costs[s][now] + costs[now][node]:
#                 costs[s][node] = costs[s][now] + costs[now][node]
#                 que.append(node)
#             else:
#                 if not visited[node]:
#                     que.append(node)
#
#
# for city in range(1, n + 1):
#     modified_bfs(city)
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if costs[i][j] == math.inf:
#             print(0, end=' ')
#         else:
#             print(costs[i][j], end=' ')
#     print()

# using Dijkstra
import sys
import heapq
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

costs = [[math.inf] * (n + 1) for _ in range(n + 1)]
routes = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    costs[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    routes[a].append(b)
    costs[a][b] = min(costs[a][b], c)


def dijkstra(s):
    que = []
    heapq.heapify(que)
    heapq.heappush(que, (costs[s][s], s))

    while que:
        now = heapq.heappop(que)[1]

        for node in routes[now]:
            if costs[s][node] > costs[s][now] + costs[now][node]:
                costs[s][node] = costs[s][now] + costs[now][node]
                heapq.heappush(que, (costs[s][node], node))


for city in range(1, n + 1):
    dijkstra(city)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if costs[i][j] == math.inf:
            print(0, end=' ')
        else:
            print(costs[i][j], end=' ')
    print()
