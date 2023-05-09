import sys

input = sys.stdin.readline

N, L = map(int, input().split())
A = list()
temp = list()
answer = list()

for i in range(N):
    temp.append(A[i])

    if len(temp) == L + 1:
        temp.pop(0)

    answer.append(min(temp))

for i in answer:
    print(i, end=' ')
