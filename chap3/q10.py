# import sys
#
# input = sys.stdin.readline
#
# N, L = map(int, input().split())
# A = list(map(int, input().split()))
# temp = list()
# answer = list()
#
# for i in range(N):
#     temp.append(A[i])
#
#     if len(temp) == L + 1:
#         temp.pop(0)
#
#     answer.append(min(temp))
#
# for i in answer:
#     print(i, end=' ')
# 내 풀이 -> 시간 초과

from collections import deque

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
