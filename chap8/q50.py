# BOJ 1717
# pypy3로 채점시 굳이 재귀 호출 깊이 설정 필요 x
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())
L = [i for i in range(n + 1)]


def union(a, b):
    if L[a] != a:
        a = find(a)
    if L[b] != b:
        b = find(b)

    if a != b:
        L[b] = a


def find(number):
    if L[number] == number:
        return number

    root = find(L[number])
    L[number] = root
    return root


for _ in range(m):
    command, a, b = map(int, input().split())

    if command == 0:
        union(a, b)
    elif command == 1:
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            print("YES")
        else:
            print("NO")
