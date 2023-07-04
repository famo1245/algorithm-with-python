# N = int(input())
#
# A = [0] * N
# S = [0] * (N - 1)
#
# for i in range(N):
#     A[i] = int(input())
#
# A.sort()
#
# S[0] = A[0] + A[1]
# idx = 1
# for i in range(2, N):
#     S[idx] = A[i] + S[idx - 1]
#     idx += 1
#
# print(sum(S))
# 순서를 고려할 때가 있음 -> 내 풀이는 최솟값이 아닌 반례 있음 (10, 10, 10, 10) 일 때
# 최솟값의 두 묶음을 계속 더해야 함

from queue import PriorityQueue

N = int(input())

A = PriorityQueue()
sum = 0

for _ in range(N):
    A.put(int(input()))

while A.qsize() > 1:
    num1 = A.get()
    num2 = A.get()

    temp = num1 + num2
    sum += temp
    A.put(temp)

print(sum)
