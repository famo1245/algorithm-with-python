import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
G = list(map(int, input().split()))
G.sort()

start_idx = 0
end_idx = N - 1
count = 0

while start_idx < end_idx:
    sum = G[start_idx] + G[end_idx]
    if sum == M:
        count += 1
        start_idx += 1
        end_idx -= 1

    elif sum > M:
        end_idx -= 1

    else:
        start_idx += 1

print(count)
