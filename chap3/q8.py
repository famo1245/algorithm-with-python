import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

for i in range(N):
    start_idx = 0
    end_idx = N - 1
    find = A[i]
    while start_idx < end_idx:
        sum = A[start_idx] + A[end_idx]
        if find == sum:
            count += 1
            start_idx = end_idx + 1
        elif find < sum:
            end_idx -= 1
        else:
            start_idx += 1

print(count)
