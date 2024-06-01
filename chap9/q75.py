# BOJ 11438
import sys
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
max_length = 0
# depth > k를 만족하는 k 구하기
while max_depth > 2 ** max_length:
    max_length += 1

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
    if a == 1 or b == 1:
        print(1)
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
            break
        k -= 1

    if k == -1:
        print(parent_list[a][0])
    else:
        print(parent_list[parent_list[a][k]][0])


def adjust_depth(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    depth_diff = depth[b] - depth[a]
    # 2^k 씩 부모 노드로 이동
    while depth_diff > 0:
        step = 0
        while depth_diff > 2 ** step:
            if step == max_length - 1:
                break
            step += 1

        b = parent_list[b][step]
        depth_diff -= 2 ** step
    return a, b


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    find_lca(a, b)
