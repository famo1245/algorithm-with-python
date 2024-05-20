# BOJ 11403
import sys
input = sys.stdin.readline

N = int(input())
G = []

for _ in range(N):
    line = list(map(int, input().split()))
    G.append(line)

for k in range(N):
    for s in range(N):
        for e in range(N):
            if G[s][e] == 0:
                if G[s][k] == 1 and G[k][e] == 1:
                    G[s][e] = 1

for line in G:
    print(*line)
