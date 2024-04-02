# BOJ 2252
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
students = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    students[a].append(b)
    degree[b] += 1

que = deque()


def get_degree_zero():
    for i in range(1, len(degree)):
        if degree[i] == 0:
            # 정렬 했음을 표시
            degree[i] = -1
            que.append(i)


get_degree_zero()
while que:
    now = que.popleft()
    answer.append(now)

    for i in students[now]:
        degree[i] -= 1

    get_degree_zero()

print(*answer)
