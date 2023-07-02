import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target_list = list(map(int, input().split()))

for t in target_list:
    start = 0
    end = len(A) - 1
    flag = 0

    while start <= end:
        mid_idx = (start + end) // 2
        median = A[mid_idx]

        if t < median:
            end = mid_idx - 1
        elif t > median:
            start = mid_idx + 1
        else:
            flag = 1
            break

    print(flag)
