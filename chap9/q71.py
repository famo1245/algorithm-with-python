# BOJ 2042
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())


def calc_length():
    result = 2
    while result < N:
        result *= 2

    return result * 2


tree_length = calc_length()
tree = [0] * tree_length

start_index = tree_length // 2
for i in range(N):
    num = int(input())
    tree[start_index + i] = num

# 세그먼트 트리 초기화
index = start_index - 1
while index > 1:
    tree[index] = tree[index * 2] + tree[index * 2 + 1]
    index -= 1


def update(index, num):
    # 세그먼트 트리에서의 인덱스와 다르므로 계산
    tree_index = index + start_index - 1
    difference = num - tree[tree_index]

    while tree_index > 1:
        tree[tree_index] += difference
        tree_index //= 2


def print_sum(start, end):
    # 세그먼트 트리에서의 인덱스와 다르므로 계산
    tree_start = start + start_index - 1
    tree_end = end + start_index - 1

    result = 0
    while tree_start <= tree_end:
        if tree_start % 2 == 1:
            result += tree[tree_start]
        if tree_end % 2 == 0:
            result += tree[tree_end]

        tree_start = (tree_start + 1) // 2
        tree_end = (tree_end - 1) // 2

    print(result)


for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    elif a == 2:
        print_sum(b, c)
