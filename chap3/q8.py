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
            if start_idx != i and end_idx != i:  # 자기 자신이 더해질 경우
                count += 1
                break
            elif start_idx == i:
                start_idx += 1
            elif end_idx == i:
                end_idx -= 1
        elif find < sum:
            end_idx -= 1
        else:
            start_idx += 1

print(count)
