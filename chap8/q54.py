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
while que:
    now = que.popleft()

    result[now] += times[now]

    for node in buildings[now]:
        result[node] = max(result[now], result[node])
        degree[node] -= 1

    find_zero_degree()

for i in range(1, len(result)):
    print(result[i])

# 사용 반례
# 3
# 10 -1
# 4 1 -1
# 100 -1
#
# 6
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
# 20 -1
#
# 5
# 10 -1
# 20 1 -1
# 30 2 -1
# 40 3 5 -1
# 100 -1
