import sys
from collections import deque
from math import inf
input = sys.stdin.readline

OFFSET = [(-1, 0), (1, 0), (0, -1), (0, 1)]
NUM_OF_VILLAIN = 3
WALL = 1
R, C = map(int, input().split())
maps = [[-1] * C for _ in range(R)]
times = [[[0] * NUM_OF_VILLAIN for _ in range(C)] for _ in range(R)]

for i in range(R):
    line = input()
    for j in range(C):
        maps[i][j] = int(line[j])


def bfs(r, c, index):
    q = deque()
    visited = [[False] * C for _ in range(R)]
    q.append((r, c, 1))
    times[r][c][index] = 1
    visited[r][c] = True

    while q:
        now_row, now_col, time = q.popleft()
        for dx, dy in OFFSET:
            next_row = now_row + dx
            next_col = now_col + dy
            if 0 <= next_row < R and 0 <= next_col < C:
                if not visited[next_row][next_col] and maps[next_row][next_col] != WALL:
                    visited[next_row][next_col] = True
                    times[next_row][next_col][index] = time + 1
                    q.append((next_row, next_col, time + 1))


for i in range(NUM_OF_VILLAIN):
    row, col = map(int, input().split())
    bfs(row - 1, col - 1, i)

min_time = inf
spot = 0
for i in range(R):
    for j in range(C):
        if maps[i][j] == WALL:
            continue

        flag = False
        for t in times[i][j]:
            if not t:
                flag = True
                break

        if flag:
            continue

        max_time = max(times[i][j])
        if min_time > max_time:
            min_time = max_time
            spot = 1
        elif min_time == max_time:
            spot += 1

if min_time == inf:
    print(-1)
else:
    print(min_time - 1)
    print(spot)
