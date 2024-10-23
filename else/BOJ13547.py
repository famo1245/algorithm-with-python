import sys
from collections import defaultdict
input = sys.stdin.readline


def process(val):
    return int(val) - 1


N = int(input())
seq = list(map(int, input().split()))
sqrt = N ** 0.5

M = int(input())
query = [[i] + list(map(process, input().split())) for i in range(M)]
query.sort(key=lambda x: (x[1] // sqrt, x[2]))

dic = defaultdict(int)
answer = [0] * M
count = 0
prev_i = 0
prev_j = -1

for index, i, j in query:
    while prev_j < j:
        prev_j += 1
        if not dic[seq[prev_j]]:
            count += 1
        dic[seq[prev_j]] += 1

    while prev_j > j:
        dic[seq[prev_j]] -= 1
        if not dic[seq[prev_j]]:
            count -= 1
        prev_j -= 1

    while prev_i < i:
        dic[seq[prev_i]] -= 1
        if not dic[seq[prev_i]]:
            count -= 1
        prev_i += 1

    while prev_i > i:
        prev_i -= 1
        if not dic[seq[prev_i]]:
            count += 1
        dic[seq[prev_i]] += 1

    answer[index] = count

print(*answer, sep='\n')
