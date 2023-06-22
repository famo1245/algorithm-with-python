# N = int(input())
# A = [0] * N
#
# for i in range(N):
#     A[i] = int(input())
#
# for i in range(N-1):
#     change = False
#     for j in range(N-1-i):
#         if A[j] > A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]
#             change = True
#
#     if change:
#         print(i-1)
#         break

# 내가 푼 문제 오류
# 파이썬의 sort 함수를 이용 하여, 원래 리스트의 인덱스와 비교 최댓값 + 1이 loop를 돈 횟수

import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max + 1)
