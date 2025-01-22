# BOJ 4386
import sys
import heapq
from math import sqrt
input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N)]
points = []

for i in range(N):
    x, y = map(float, input().split())
    points.append((x, y))

edges = []
for i in range(N):
    from_x, from_y = points[i]

    for j in range(N):
        to_x, to_y = points[j]
        d = sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2)
        edges.append((d, i, j))


def find(a):
    if parent[a] == a:
        return a

    root = find(parent[a])
    parent[a] = root
    return root


def union(a, b):
    if parent[a] != a:
        a = find(a)
    if parent[b] != b:
        b = find(b)

    if a != b:
        parent[a] = b


heapq.heapify(edges)
count = 0
cost = 0
while count < N - 1:
    d, a, b = heapq.heappop(edges)
    if find(a) != find(b):
        union(a, b)
        cost += d
        count += 1

print(round(cost, 2))
