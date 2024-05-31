# BOJ 11437
# 리스트에 튜플 삽입
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# N = int(input())
# tree = [[] for _ in range(N + 1)]
#
# for _ in range(N - 1):
#     s, e = map(int, input().split())
#     tree[s].append(e)
#     tree[e].append(s)
#
# parent_list = [0] * (N + 1)
# root = 1
# parent_list[root] = (-1, 0)
# que = deque()
# que.append(root)
#
# # BFS 이용 탐색
# while que:
#     now = que.popleft()
#
#     for node in tree[now]:
#         depth = parent_list[now][1]
#         # parent list 초기화
#         if parent_list[node] == 0:
#             parent_list[node] = (now, depth + 1)
#             que.append(node)
#
#
# def find_lca(a, b):
#     if a == root or b == root:
#         print(root)
#         return
#
#     # 두 노드의 level이 다를 때
#     if parent_list[a][1] != parent_list[b][1]:
#         if parent_list[a][1] > parent_list[b][1]:
#             a, b = b, a
#
#         # 두 노드의 level을 맞춤
#         while parent_list[a][1] != parent_list[b][1]:
#             # level을 맞추던 중 두 노드가 만나게 되면 lca
#             if a == parent_list[b][0]:
#                 print(a)
#                 return
#
#             b = parent_list[b][0]
#
#     # 부모 노드로 이동하며 최소 공통 조상을 찾음
#     while a != b:
#         a = parent_list[a][0]
#         b = parent_list[b][0]
#
#     print(a)
#
#
# M = int(input())
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     find_lca(a, b)

# 리스트 따로 사용
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

parent_list = [0] * (N + 1)
depth = [-1] * (N + 1)
root = 1
parent_list[root] = -1
depth[root] = 0
que = deque()
que.append(root)

# BFS 이용 탐색
while que:
    now = que.popleft()

    for node in tree[now]:
        level = depth[now]
        # parent list 초기화
        if parent_list[node] == 0:
            parent_list[node] = now
            depth[node] = level + 1
            que.append(node)


def find_lca(a, b):
    if a == root or b == root:
        print(root)
        return

    # 두 노드의 level이 다를 때
    if depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a, b = b, a

        # 두 노드의 level을 맞춤
        while depth[a] != depth[b]:
            b = parent_list[b]

    # 부모 노드로 이동하며 최소 공통 조상을 찾음
    while a != b:
        a = parent_list[a]
        b = parent_list[b]

    print(a)


M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    find_lca(a, b)
