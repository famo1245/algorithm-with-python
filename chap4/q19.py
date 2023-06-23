# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# A.sort()
#
# for i in range(N):
#     if i == (K - 1):
#         print(A[i])

# 퀵 정렬로 시간 줄여보기, 큰 차이 없더라

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))


def quick_sort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:
            return
        elif K < pivot:
            quick_sort(S, pivot - 1, K)
        else:
            quick_sort(pivot + 1, E, K)


def swap(i, j):
    global A
    A[i], A[j] = A[j], A[i]


def partition(S, E):
    global A

    if S + 1 == E:
        if A[S] > A[E]:
            swap(S, E)
        return E

    M = (S + E) // 2
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E

    while i <= j:
        while pivot < A[j] and j > 0:
            j -= 1
        while pivot > A[i] and i < len(A) - 1:
            i += 1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1

    A[S] = A[j]
    A[j] = pivot
    return j


quick_sort(0, N-1, K-1)
print(A[K-1])
