# BOJ 1806
import sys
from math import inf
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
result, start, end = 0, 0, 0
answer = inf

while True:
    if result >= S:
        answer = min(answer, end - start)
        result -= nums[start]
        start += 1
    else:
        if end == N:
            break
        result += nums[end]
        end += 1

if answer == inf:
    print(0)
else:
    print(answer)
