import sys

input = sys.stdin.readline

A = [0] * 10001

N = int(input())

for _ in range(N):
    A[int(input())] += 1

for i in range(len(A)):
    if A[i] != 0:
        for _ in range(A[i]):
            print(i)
