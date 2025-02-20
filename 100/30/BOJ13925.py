# BOJ 13925
import sys
input = sys.stdin.readline

ADD = 1
MUL = 2
REPLACE = 3
PRINT = 4
MOD = 10 ** 9 + 7
N = int(input())
input_list = list(map(int, input().split()))
tree = [0] * (N * 4)
lazy = [[1, 0] for _ in range(N * 4)]


def init(node, start, end):
    if start == end:
        tree[node] = input_list[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = (init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)) % MOD
    return tree[node]


def update_lazy(node, start, end):
    if lazy[node][0] != 1 or lazy[node][1] != 0:
        tree[node] = (tree[node] * lazy[node][0] + lazy[node][1] * (end - start + 1)) % MOD

        if start != end:
            lazy[node * 2][0] = lazy[node * 2][0] * lazy[node][0] % MOD
            lazy[node * 2][1] = (lazy[node * 2][1] * lazy[node][0] + lazy[node][1]) % MOD

            lazy[node * 2 + 1][0] = lazy[node * 2 + 1][0] * lazy[node][0] % MOD
            lazy[node * 2 + 1][1] = (lazy[node * 2 + 1][1] * lazy[node][0] + lazy[node][1]) % MOD

        lazy[node][0] = 1
        lazy[node][1] = 0


def update(node, start, end, left, right, value, operation):
    update_lazy(node, start, end)
    if left > end or right < start:
        return

    if left <= start and end <= right:
        if operation == ADD:
            lazy[node][1] = (lazy[node][1] + value) % MOD
        elif operation == MUL:
            lazy[node][0] = (lazy[node][0] * value) % MOD
        elif operation == REPLACE:
            lazy[node][0] = 0
            lazy[node][1] = value

        update_lazy(node, start, end)
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, value, operation)
    update(node * 2 + 1, mid + 1, end, left, right, value, operation)
    tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD


def query(node, start, end, left, right):
    update_lazy(node, start, end)
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node] % MOD

    mid = (start + end) // 2
    return (query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)) % MOD


init(1, 0, N - 1)

M = int(input())
for _ in range(M):
    command, *nums = map(int, input().split())
    if command == PRINT:
        print(query(1, 0, N - 1, nums[0] - 1, nums[1] - 1))
    else:
        update(1, 0, N - 1, nums[0] - 1, nums[1] - 1, nums[2], command)
