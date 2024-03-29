# BOJ 1976
# BFS 이용
# 1. 24번째 줄 cities[start][end]로 조건 설정 오류
# 2. 44번째 줄 i의 범위 설정 오류
# 3. routes 입력 1 1 같은 경우 고려 x

# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
# cities = [[0] for _ in range(n + 1)]
#
#
# def check_path(start, end):
#     if start == end:
#         return True
#
#     que = deque()
#     que.append(start)
#     visited = [False] * (n + 1)
#     visited[start] = True
#
#     while que:
#         now = que.popleft()
#         if cities[now][end] == 1:
#             return True
#
#         for i in range(1, len(cities[now])):
#                 if cities[now][i] == 1 and not visited[i]:
#                     visited[i] = True
#                     que.append(i)
#
#     return False
#
#
# for i in range(1, n + 1):
#     line = list(map(int, input().split()))
#     cities[i] += line
#
# routes = list(map(int, input().split()))
#
# possible = True
#
# for i in range(len(routes) - 1):
#     possible = check_path(routes[i], routes[i + 1])
#
#     if not possible:
#         break
#
# if possible:
#     print("YES")
# else:
#     print("NO")

# union-find 이용
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
L = [i for i in range(n + 1)]


def union(a, b):
    if L[a] != a:
        a = find(a)
    if L[b] != b:
        b = find(b)

    if a != b:
        L[b] = a


def find(a):
    if L[a] == a:
        return a

    root = find(L[a])
    L[a] = root
    return root


for i in range(1, n + 1):
    temp = [0] + list(map(int, input().split()))
    # cities[i] += temp

    for j in range(1, len(temp)):
        if temp[j] == 1:
            union(i, j)

routes = list(map(int, input().split()))

possible = True
for i in range(len(routes) - 1):
    start = find(routes[i])
    end = find(routes[i + 1])

    if start != end:
        possible = False
        break

if possible:
    print("YES")
else:
    print("NO")