# BOJ 11657
import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

routes = []
answer = [math.inf] * (N + 1)
answer[1] = 0

for _ in range(M):
    s, e, w = map(int, input().split())
    routes.append((s, e, w))

for _ in range(N):
    for s, e, w in routes:
        if answer[s] != math.inf and answer[e] > answer[s] + w:
            answer[e] = answer[s] + w

has_cycle = False

for s, e, w in routes:
    if answer[s] != math.inf and answer[e] > answer[s] + w:
        has_cycle = True

if has_cycle:
    print(-1)
    exit(0)

for i in range(2, N + 1):
    element = answer[i]
    if element == math.inf:
        print(-1)
        continue

    print(element)
