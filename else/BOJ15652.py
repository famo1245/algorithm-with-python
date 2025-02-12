import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = []


def rec(index, count):
    if count == M:
        print(*l)
        return

    for i in range(index, N + 1):
        l.append(i)
        rec(i, count + 1)
        l.pop()


rec(1, 0)
