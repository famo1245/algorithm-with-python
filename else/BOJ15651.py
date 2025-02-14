# BOJ 15651
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = []


def rec(count):
    if count == M:
        print(*l)
        return

    for i in range(1, N + 1):
        l.append(i)
        rec(count + 1)
        l.pop()


rec(0)
