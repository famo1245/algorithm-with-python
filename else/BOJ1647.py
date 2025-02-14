# BOJ 1647
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
routes = []

for _ in range(M):
    a, b, cost = map(int, input().split())
    heapq.heappush(routes, (cost, a, b))

parent = [i for i in range(N + 1)]


def find(a):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


count = 0
answer = 0
last = 0
while count < N - 1 and routes:
    cost, a, b = heapq.heappop(routes)

    if find(a) != find(b):
        union(a, b)
        answer += cost
        last = cost
        count += 1

answer -= last
print(answer)
