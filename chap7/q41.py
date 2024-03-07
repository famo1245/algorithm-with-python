# BOJ 11689
# 메모리 초과 -> 배열 사용 때문인듯

# N = int(input())
# P = [0] * (N + 1)
#
# for i in range(1, len(P)):
#     P[i] = i
#
# for i in range(2, len(P)):
#     if P[i] == i:
#         for j in range(i, len(P), i):
#             P[j] = P[j] - int(P[j]/i)
#
# print(P[N])
import math

N = int(input())
answer = N

for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        answer -= int(answer/i)
        while N % i == 0:
            N /= i

if N > 1:
    answer -= int(answer/N)

print(answer)
