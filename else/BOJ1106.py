import sys
from math import inf
input = sys.stdin.readline

MAX = 100000
c, n = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(n)]

D = [inf] * (MAX + 1)
D[0] = 0

for i in range(1, MAX + 1):
    for cost, people in info:
        D[i] = min(D[i], D[i - people] + cost)

print(min(D[c:]))