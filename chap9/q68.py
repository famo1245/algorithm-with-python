# BOJ 1068
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
input_list = list(map(int, input().split()))
delete_node = int(input())
tree = [[] for _ in range(N)]

for i in range(len(input_list)):
    parent = input_list[i]
    # root node 처리
    if parent == -1:
        root_node = i
        continue

    child = i
    tree[parent].append(child)

# 삭제 노드가 root node인 경우
if delete_node == root_node:
    print(0)
    exit(0)

que = deque()
que.append(delete_node)

# parent node에서 연결 정보 삭제
parent_node = input_list[delete_node]
tree[parent_node].remove(delete_node)

while que:
    now = que.popleft()
    for node in tree[now]:
        que.append(node)

    tree[now] = -1

leaf_nodes = 0
for i in range(N):
    if not tree[i]:
        leaf_nodes += 1

print(leaf_nodes)

# 사용 반례
# root 노드에 자식이 하나 -> 이 노드가 삭제 노드일 때
# 5
# -1 0 1 2 3
# 1
# output: 0
