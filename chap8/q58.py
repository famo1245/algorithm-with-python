# BOJ 1854
# import sys
# import math
# from queue import PriorityQueue
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
# visited = [False] * (n + 1)
# routes = [[] for _ in range(n + 1)]
# times = [[math.inf] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     routes[a].append((b, c))
#
# start = 1
# times[start][0] = 0
# que = PriorityQueue()
# que.put((times[start][0], start))
#
# while not que.empty():
#     now = que.get()[1]
#     if visited[now]:
#         continue
#     visited[now] = True
#
#     for node, value in routes[now]:
#         for now_time in times[now]:
#             if now_time == math.inf:
#                 continue
#
#             if times[node][0] > now_time + value:
#                 times[node].insert(0, now_time + value)
#
#                 if not visited[node]:
#                     que.put((times[node][0], node))
#             else:
#                 times[node].append(now_time + value)
#
# for i in range(1, len(times)):
#     time = times[i]
#
#     if len(time) < k:
#         print(-1)
#         continue
#
#     time.sort()
#     if time[k - 1] == math.inf:
#         print(-1)
#     else:
#         print(time[k - 1])

import sys
import math
from queue import PriorityQueue

input = sys.stdin.readline

n, m, k = map(int, input().split())
# visited = [False] * (n + 1)
routes = [[] for _ in range(n + 1)]
times = [[math.inf] * k for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    routes[a].append((b, c))

start = 1
times[start][0] = 0
que = PriorityQueue()
que.put((times[start][0], start))

while not que.empty():
    now_time, now = que.get()
    # if visited[now]:
    #     continue
    # visited[now] = True

    for node, value in routes[now]:
        times[node].sort()
        if times[node][k - 1] > now_time + value:
            times[node][k - 1] = now_time + value
            # if not visited[node]:
            #     que.put((times[node][k - 1], node))
            que.put((times[node][k - 1], node))

for i in range(1, len(times)):
    time = times[i]
    if time[k - 1] == math.inf:
        print(-1)
    else:
        print(time[k - 1])
