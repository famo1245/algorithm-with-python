# # SW academy D2 1959
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    D = [0] * (M - N + 1)

    for j in range(M - N + 1):
        result = 0
        for k in range(N):
            result += A[k] * B[k + j]
        D[j] = max(result, D[j - 1])

    print(f'#{test_case} {D[M - N]}')
