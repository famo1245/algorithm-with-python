import sys
from math import inf
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, *A = map(int, input().split())
    A.sort()

    S = [A[0]]
    for i in range(1, N):
        S.append(S[i - 1] + A[i])

    answer = 0
    for i in range(2, N + 1):
        result = inf
        for j in range(i - 1, N):
            temp = A[j] * i - S[j]
            if j - i > -1:
                temp += S[j - i]

            result = min(result, temp)

        answer += result

    print(answer)
