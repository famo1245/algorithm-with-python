N = int(input())
k = int(input())

start = 1
end = k
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(1, N + 1):
        # less = mid // i
        # if less > N:
        #     less = N
        # count += less
        count += min((mid // i), N)  # 이런식으로 위의 조건문 대체 가능

    if count < k:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)
