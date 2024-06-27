# # SW academy D2 1959
# import sys
# input = sys.stdin.readline
#
# T = int(input())
# for i in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     D = [0] * (M - N + 1)
#
#     if N > M:
#         N, M = M, N
#         A, B = B, A
#
#     for j in range(M - N + 1):
#         result = 0
#         for k in range(N):
#             result += A[k] * B[k + j]
#         D[j] = result
#
#     print(D)
#     print(f'#{i + 1} {max(D)}')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
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
        D[j] = result

    print(f'#{test_case} {max(D)}')