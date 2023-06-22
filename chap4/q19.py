N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

for i in range(N):
    if i == (K - 1):
        print(A[i])

# 퀵 정렬로 시간 줄여보기
