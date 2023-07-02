import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

start = max(A)
end = sum(A)

while start <= end:
    mid = (start + end) // 2
    sum_lesson = 0
    count = 0
    for i in range(N):
        if sum_lesson + A[i] > mid:
            count += 1
            sum_lesson = 0
        sum_lesson += A[i]

    if sum_lesson != 0:
        count += 1
    if count > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)
