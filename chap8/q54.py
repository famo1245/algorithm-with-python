# BOJ 1516
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
times = [0] * (N + 1)
degree = [0] * (N + 1)
buildings = [[] for _ in range(N + 1)]
result = [0] * (N + 1)

for i in range(1, N + 1):
    line = list(map(int, input().split()))

    for j in range(len(line)):
        if line[j] == -1:
            break
        if j == 0:
            times[i] = line[j]
            continue

        buildings[line[j]].append(i)
        degree[i] += 1

que = deque()


def find_zero_degree():
    for i in range(1, len(degree)):
        if degree[i] == 0:
            degree[i] = -1
            que.append(i)


find_zero_degree()
time_sum = 0
while que:
    now = que.popleft()

    if len(que) == 0:
        time_sum += times[now]
        result[now] = time_sum
    else:
        result[now] = time_sum + times[now]

    for node in buildings[now]:
        degree[node] -= 1

    find_zero_degree()

for i in range(1, len(result)):
    print(result[i])
