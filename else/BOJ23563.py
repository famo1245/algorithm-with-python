# BOJ 23563
import sys
from collections import deque
from math import inf

input = sys.stdin.readline

OFFSET = [(1, 0), (-1, 0), (0, 1), (0, -1)]
WALL = '#'
END = 'E'
START = 'S'


def is_near_wall(maps, row, col, H, W):
    for dr, dc in OFFSET:
        nr, nc = row + dr, col + dc
        if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] == WALL:
            return True
    return False


H, W = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(H)]
start, end = None, None
for r in range(H):
    for c in range(W):
        if maps[r][c] == START:
            start = (r, c)
        elif maps[r][c] == END:
            end = (r, c)

distance = [[inf] * W for _ in range(H)]
q = deque([(start[0], start[1], 0)])
distance[start[0]][start[1]] = 0

while q:
    row, col, hop = q.popleft()

    if distance[row][col] < hop:
        continue

    cur_near_wall = is_near_wall(maps, row, col, H, W)

    for dr, dc in OFFSET:
        nr, nc = row + dr, col + dc

        if not (0 <= nr < H and 0 <= nc < W):
            continue
        if maps[nr][nc] == WALL:
            continue

        next_hop = hop
        if not (cur_near_wall and is_near_wall(maps, nr, nc, H, W)):
            next_hop += 1

        if distance[nr][nc] > next_hop:
            distance[nr][nc] = next_hop
            if next_hop > hop:
                q.append((nr, nc, next_hop))
            else:
                q.appendleft((nr, nc, next_hop))

print(distance[end[0]][end[1]])

