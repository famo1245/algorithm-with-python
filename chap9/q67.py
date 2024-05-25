# BOJ 11725
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

parent = [0] * (N + 1)
start = 1

que = deque()
parent[start] = -1
que.append(start)

while que:
    now = que.popleft()

    for node in tree[now]:
        if parent[node] == 0:
            parent[node] = now
            que.append(node)

for i in range(2, N + 1):
    print(parent[i])
