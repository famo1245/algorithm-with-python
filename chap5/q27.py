import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
A = []
visit = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    line = input()
    temp = list()
    for i in range(M):
        temp.append(int(line[i]))
    A.append(temp)


def bfs(x, y):
    my_queue = deque()
    my_queue.append((x, y))
    visit[x][y] = True

    while my_queue:
        node = my_queue.popleft()
        for i in range(4):
            x1 = node[0] + dx[i]
            y1 = node[1] + dy[i]

            if 0 <= x1 < N and 0 <= y1 < M:
                if A[x1][y1] != 0 and not visit[x1][y1]:
                    visit[x1][y1] = True
                    A[x1][y1] = A[node[0]][node[1]] + 1
                    my_queue.append((x1, y1))


bfs(0, 0)
print(A[N-1][M-1])
