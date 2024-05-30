# BOJ 10868
import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())


def calc_length():
    result = 2
    while result < N:
        result *= 2

    return result * 2


tree_length = calc_length()
start_index = tree_length // 2
tree = [math.inf] * tree_length

# segment tree 초기화
for i in range(N):
    num = int(input())
    tree[start_index + i] = num

index = start_index - 1
while index > 1:
    tree[index] = min(tree[index * 2], tree[index * 2 + 1])
    index -= 1


def print_min(start, end):
    tree_start = start + start_index - 1
    tree_end = end + start_index - 1

    result = math.inf
    while tree_start <= tree_end:
        if tree_start % 2 == 1:
            result = min(result, tree[tree_start])
        if tree_end % 2 == 0:
            result = min(result, tree[tree_end])

        tree_start = (tree_start + 1) // 2
        tree_end = (tree_end - 1) // 2

    print(result)


for _ in range(M):
    s, e = map(int, input().split())
    print_min(s, e)
