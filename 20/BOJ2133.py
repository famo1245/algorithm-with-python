# BOJ 2133
import sys
input = sys.stdin.readline

N = int(input())
D = [0] * 31
D[0] = 1
D[2] = 3

for i in range(4, N + 1, 2):
    D[i] = D[i - 2] * 3
    for j in range(4, i + 1, 2):
        D[i] += D[i - j] * 2

print(D[N])
