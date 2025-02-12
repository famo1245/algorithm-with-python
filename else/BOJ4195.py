# BOJ 4195
import sys
input = sys.stdin.readline

index = {}
parent = []


def find(a):
    if parent[a] < 0:
        return a

    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if parent[a] < parent[b]:
            parent[a] += parent[b]
            parent[b] = a
        else:
            parent[b] += parent[a]
            parent[a] = b

    print(-parent[find(a)])


for _ in range(int(input())):
    F = int(input())
    parent = [-1] * (F * 2)
    count = 0

    for _ in range(F):
        a, b = input().split()

        if a not in index:
            index[a] = count
            count += 1

        if b not in index:
            index[b] = count
            count += 1

        union(index[a], index[b])

    index.clear()
