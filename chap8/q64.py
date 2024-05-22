# BOJ 1197
# import sys
# input = sys.stdin.readline
#
# V, E = map(int, input().split())
# edge_list = []
# node = [i for i in range(V + 1)]
#
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     edge_list.append((a, b, c))
#
#
# def find(e):
#     if node[e] == e:
#         return e
#
#     root = find(node[e])
#     node[e] = root
#     return root
#
#
# def union(a, b):
#     if node[a] != a:
#         a = find(a)
#     if node[b] != b:
#         b = find(b)
#
#     if a != b:
#         node[a] = b
#
#
# edge_list.sort(key=lambda x: x[2])
# minimum_spanning_tree = 0
#
# for s, e, w in edge_list:
#     if find(s) != find(e):
#         union(s, e)
#         minimum_spanning_tree += w
#
# print(minimum_spanning_tree)

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge_list = []
heapq.heapify(edge_list)
node = [i for i in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(edge_list, (c, a, b))


def find(e):
    if node[e] == e:
        return e

    root = find(node[e])
    node[e] = root
    return root


def union(a, b):
    if node[a] != a:
        a = find(a)
    if node[b] != b:
        b = find(b)

    if a != b:
        node[a] = b


minimum_spanning_tree = 0
count = 0
while count < V - 1:
    w, s, e = heapq.heappop(edge_list)
    if find(s) != find(e):
        union(s, e)
        minimum_spanning_tree += w
        count += 1

print(minimum_spanning_tree)
