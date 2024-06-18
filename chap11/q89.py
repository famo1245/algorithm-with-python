# BOJ 13398
import sys
from math import inf

input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))
left = [0] * N
right = [0] * N
D = [0] * N

left[0] = l[0]
right[N - 1] = l[N - 1]

max_left = -inf
max_right = -inf
for i in range(1, N):
    left[i] = max(l[i], left[i - 1] + l[i])
    right[N - i - 1] = max(l[N - i - 1], right[N - i] + l[N - i - 1])

    if max_left < left[i]:
        max_left = left[i]
    if max_right < right[N - i - 1]:
        max_right = right[N - i - 1]

max_D = -inf
for i in range(N):
    if i == 0:
        D[i] = right[i]
    elif i == N - 1:
        D[i] = left[i]
    else:
        D[i] = left[i - 1] + right[i + 1]

    if max_D < D[i]:
        max_D = D[i]

print(max(max_left, max_right, max_D))

# 반례
# input
# 4
# -1 -1 1 -1
# output
# 1
