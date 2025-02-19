# BOJ 1033
import sys
input = sys.stdin.readline


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


N = int(input())
G = [[] for _ in range(N)]
l = 1

for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    G[a].append((b, p, q))
    G[b].append((a, q, p))
    l *= lcm(p, q)

visited = [False] * N
answer = [0] * N
answer[0] = l
stack = [0]
while stack:
    now = stack.pop()
    visited[now] = True

    for next, q, p in G[now]:
        if not visited[next]:
            answer[next] = answer[now] * p // q
            stack.append(next)

g = answer[0]
for i in range(1, N):
    g = gcd(g, answer[i])

answer = [i // g for i in answer]
print(*answer)
