# BOJ 1707
# 메모리 초과

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# # group = False
# group = 1  # 배열 수를 줄이기 위해 변수 사용
#
# k = int(input())
#
#
# def dfs(node):
#     global group
#     # visited[node][0] = True
#     # visited[node].append(group)
#     # check[node] = group
#     visited[node] = group
#     group = -group
#     for i in G[node]:
#         # if not visited[i][0]:
#         if visited[i] == 0:
#             dfs(i)
#         else:
#             # if visited[i][1] == visited[node][1]:
#             # if check[i] == check[node]:
#             if visited[i] == visited[node]:
#                 return False
#
#     return True
#
#
# for _ in range(k):
#     v, e = map(int, input().split())
#     G = [[] for _ in range(v + 1)]
#     # visited = [[False] for _ in range(v + 1)]
#     # visited = [False] * (v + 1)
#     # check = [] * (v + 1)
#     visited = [0] * (v + 1)
#
#     for _ in range(e):
#         a, b = map(int, input().split())
#         G[a].append(b)
#         G[b].append(a)
#
#     flag = True
#     for i in range(1, v + 1):
#         result = dfs(i)
#         if not result:
#             print("NO")
#             flag = False
#             break
#
#     if flag:
#         print("YES")

# import sys
# # sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
# # group = 1  # 배열 수를 줄이기 위해 변수 사용
#
# k = int(input())
#
#
# def dfs(node, group):
#     # global group
#     visited[node] = group
#     # group = -group
#     for i in G[node]:
#         if visited[i] == 0:
#             return dfs(i, -group)
#         else:
#             if visited[i] == visited[node]:
#                 return False
#
#     return True
#
#
# for _ in range(k):
#     v, e = map(int, input().split())
#     G = [[] for _ in range(v + 1)]
#     visited = [0] * (v + 1)
#
#     for _ in range(e):
#         a, b = map(int, input().split())
#         G[a].append(b)
#         G[b].append(a)
#
#     flag = True
#     for i in range(1, v + 1):
#         if visited[i] == 0:
#             result = dfs(i, 1)
#             if not result:
#                 print("NO")
#                 flag = False
#                 break
#
#             if flag:
#                 print("YES")

# 이미 분할된 그래프인데 cyccle이 있는 경우 no
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())


def dfs(node, group):
    visited[node] = group
    for i in G[node]:
        if visited[i] == 0:
            return dfs(i, -group)
        else:
            if visited[i] == visited[node]:
                return False
    return True


for _ in range(k):
    v, e = map(int, input().split())
    G = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    flag = True
    # TODO: 다른 그룹인거 구분하기
    for i in range(1, v + 1):
        if visited[i] == 0:
            result = dfs(i, 1)
            if not result and i == 1:
                print("NO")
                flag = False
                break

    if flag:
        print("YES")
