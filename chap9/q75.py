# BOJ 11438
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# N = int(input())
# root = 1
# tree = [[] for _ in range(N + 1)]
# parent_list = [0] * (N + 1)
# depth = [-1] * (N + 1)
#
# for _ in range(N - 1):
#     s, e = map(int, input().split())
#     tree[s].append(e)
#     tree[e].append(s)
#
# # tree 초기화
# depth[root] = 0
# parent_list[root] = -1
# que = deque()
# que.append(root)
# while que:
#     now = que.popleft()
#     now_depth = depth[now]
#
#     for node in tree[now]:
#         if parent_list[node] == 0:
#             # 2^0 번째 부모 노드 추가
#             parent_list[node] = [now]
#             depth[node] = now_depth + 1
#             que.append(node)
#
# max_depth = max(depth)
# # parent list에서 각 노드의 리스트 최대 길이
# max_length = 0
# # depth > k를 만족하는 k 구하기
# while max_depth > 2 ** max_length:
#     max_length += 1
#
# # parent list 값 채우기
# parent_list[root] = [-1] * max_length
# k = 1
# while k < max_length:
#     for i in range(root + 1, N + 1):
#         if depth[i] - 2 ** k < 0:
#             parent_list[i].append(-1)
#         else:
#             parent_list[i].append(parent_list[parent_list[i][k - 1]][k - 1])
#     k += 1
#
#
# def find_lca(a, b):
#     if a == root or b == root:
#         print(root)
#         return
#
#     if depth[a] != depth[b]:
#         a, b = adjust_depth(a, b)
#
#     if a == b:
#         print(a)
#         return
#
#     # 2^k씩 부모 노드로 이동
#     k = max_length - 1
#     while k >= 0:
#         if parent_list[a][k] != parent_list[b][k]:
#             a = parent_list[a][k]
#             b = parent_list[b][k]
#         k -= 1
#
#     if a == b:
#         print(a)
#     else:
#         print(parent_list[a][0])
#
#
# def adjust_depth(a, b):
#     if depth[a] > depth[b]:
#         a, b = b, a
#
#     depth_diff = depth[b] - depth[a]
#     # 2^k 씩 부모 노드로 이동
#     while depth_diff > 0:
#         step = 0
#         for step in range(max_length - 1):
#             if depth_diff < 2 ** step:
#                 step -= 1
#                 break
#
#         b = parent_list[b][step]
#         depth_diff -= 2 ** step
#     return a, b
#
#
# M = int(input())
# for _ in range(M):
#     a, b = map(int, input().split())
#     find_lca(a, b)

import sys
from math import log2, ceil
from collections import deque
input = sys.stdin.readline

N = int(input())
root = 1
tree = [[] for _ in range(N + 1)]
parent_list = [0] * (N + 1)
depth = [-1] * (N + 1)

for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# tree 초기화
depth[root] = 0
parent_list[root] = -1
que = deque()
que.append(root)
while que:
    now = que.popleft()
    now_depth = depth[now]

    for node in tree[now]:
        if parent_list[node] == 0:
            # 2^0 번째 부모 노드 추가
            parent_list[node] = [now]
            depth[node] = now_depth + 1
            que.append(node)

max_depth = max(depth)
# parent list에서 각 노드의 리스트 최대 길이
max_length = ceil(log2(max_depth))

# parent list 값 채우기
parent_list[root] = [-1] * max_length
k = 1
while k < max_length:
    for i in range(root + 1, N + 1):
        if depth[i] - 2 ** k < 0:
            parent_list[i].append(-1)
        else:
            parent_list[i].append(parent_list[parent_list[i][k - 1]][k - 1])
    k += 1


def find_lca(a, b):
    if a == root or b == root:
        print(root)
        return

    if depth[a] != depth[b]:
        a, b = adjust_depth(a, b)

    if a == b:
        print(a)
        return

    # 2^k씩 부모 노드로 이동
    k = max_length - 1
    while k >= 0:
        if parent_list[a][k] != parent_list[b][k]:
            a = parent_list[a][k]
            b = parent_list[b][k]
        k -= 1

    if a == b:
        print(a)
    else:
        print(parent_list[a][0])


def adjust_depth(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    depth_diff = depth[b] - depth[a]
    # 2^k 씩 부모 노드로 이동
    while depth_diff > 0:
        step = int(log2(depth_diff))
        if step >= max_length - 1:
            step = max_length - 2

        b = parent_list[b][step]
        depth_diff -= 2 ** step
    return a, b


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    find_lca(a, b)

# 반례
# 7
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 6 7
# 3
# 3 6
# 4 7
# 2 7
# 출력
# 3
# 4
# 2

# 14
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 6 7
# 7 8
# 8 9
# 9 10
# 6 11
# 11 12
# 12 13
# 13 14
# 1
# 10 14
# 출력
# 6