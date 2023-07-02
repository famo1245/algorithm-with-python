import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
near_list = [[] for _ in range(N + 1)]

for _ in range(N):
    line = list(map(int, input().split()))

    node = line[0]
    idx = 1

    while line[idx] != -1:
        near_list[node].append((line[idx], line[idx + 1]))
        idx += 2

visit = [False] * (N + 1)
distance = [0] * (N + 1)


def bfs(n):
    my_queue = deque()
    my_queue.append(n)
    visit[n] = True
    while my_queue:
        now = my_queue.popleft()
        for node in near_list[now]:
            if not visit[node[0]]:
                visit[node[0]] = True
                my_queue.append(node[0])
                distance[node[0]] = distance[now] + node[1]


bfs(1)
max_node = -1

if max_node < max(distance):
    max_node = distance.index(max(distance))

visit = [False] * (N + 1)
distance = [0] * (N + 1)

bfs(max_node)
print(max(distance))
# 책 참고함
