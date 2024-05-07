# BOJ 1753
# 시간 초과
# import sys
# import math
# from collections import deque
# input = sys.stdin.readline
#
# V, E = map(int, input().split())
# visited = [False] * (V + 1)
# distance = [math.inf] * (V + 1)
# g = [[] for _ in range(V + 1)]
#
# k = int(input())
# distance[k] = 0
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     g[u].append((v, w))
#
#
# def find_min_distance_node():
#     index_list = []
#     for i in range(1, len(visited)):
#         if not visited[i]:
#             index_list.append(i)
#
#     min_distance = math.inf
#     node_num = -1
#     for i in index_list:
#         if distance[i] < min_distance:
#             min_distance = distance[i]
#             node_num = i
#
#     return node_num
#
#
# que = deque()
# que.append(k)
#
# while que:
#     now = que.popleft()
#     visited[now] = True
#
#     for t in g[now]:
#         node, value = t[0], t[1]
#         distance[node] = min(distance[node], distance[now] + value)
#
#     next = find_min_distance_node()
#     if next != -1:
#         que.append(next)
#
# for i in range(1, V + 1):
#     if distance[i] == math.inf:
#         print("INF")
#         continue
#
#     print(distance[i])

import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False] * (V + 1)
distance = [math.inf] * (V + 1)
g = [[] for _ in range(V + 1)]

k = int(input())
distance[k] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

que = PriorityQueue()
que.put((distance[k], k))

while not que.empty():
    now = que.get()[1]

    if visited[now]:
        continue

    visited[now] = True

    for t in g[now]:
        node, value = t[0], t[1]

        if distance[node] > distance[now] + value:
            distance[node] = distance[now] + value
            que.put((distance[node], node))

for i in range(1, V + 1):
    if distance[i] == math.inf:
        print("INF")
        continue

    print(distance[i])
