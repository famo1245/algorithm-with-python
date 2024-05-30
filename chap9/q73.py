# BOJ 11505
# 시간 초과
# import sys
# input = sys.stdin.readline
#
# N, M, K = map(int, input().split())
# divisor = 1000000007
#
#
# def calc_length():
#     result = 2
#     while result < N:
#         result *= 2
#
#     return result * 2
#
#
# tree_length = calc_length()
# start_index = tree_length // 2
# tree = [0] * tree_length
#
# for i in range(N):
#     num = int(input())
#     tree[start_index + i] = num
#
# index = start_index - 1
# while index > 1:
#     tree[index] = tree[index * 2] * tree[index * 2 + 1]
#     index -= 1
#
#
# def update(index, num):
#     tree_index = index + start_index - 1
#     tree[tree_index] = num
#
#     while tree_index > 1:
#         tree_index //= 2
#         tree[tree_index] = tree[tree_index * 2] * tree[tree_index * 2 + 1]
#
#
# def print_mul(start, end):
#     tree_start = start + start_index - 1
#     tree_end = end + start_index - 1
#
#     result = 1
#     while tree_start <= tree_end:
#         if tree_start % 2 == 1:
#             result *= tree[tree_start]
#         if tree_end % 2 == 0:
#             result *= tree[tree_end]
#
#         tree_start = (tree_start + 1) // 2
#         tree_end = (tree_end - 1) // 2
#
#     print(result % divisor)
#
#
# for _ in range(M + K):
#     a, b, c = map(int, input().split())
#     if a == 1:
#         update(b, c)
#     elif a == 2:
#         print_mul(b, c)
#

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
divisor = 1000000007


def calc_length():
    result = 2
    while result < N:
        result *= 2

    return result * 2


tree_length = calc_length()
start_index = tree_length // 2
tree = [1] * tree_length

for i in range(N):
    num = int(input())
    tree[start_index + i] = num

index = start_index - 1
while index > 0:
    tree[index] = tree[index * 2] * tree[index * 2 + 1] % divisor
    index -= 1


def update(index, num):
    index = index + start_index - 1
    tree[index] = num

    while index > 1:
        index //= 2
        tree[index] = tree[index * 2] * tree[index * 2 + 1] % divisor


def print_mul(start, end):
    tree_start = start + start_index - 1
    tree_end = end + start_index - 1

    result = 1
    while tree_start <= tree_end:
        if tree_start % 2 == 1:
            result = result * tree[tree_start] % divisor
            tree_start += 1
        if tree_end % 2 == 0:
            result = result * tree[tree_end] % divisor
            tree_end -= 1

        tree_start //= 2
        tree_end //= 2

    print(result)


for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    elif a == 2:
        print_mul(b, c)
