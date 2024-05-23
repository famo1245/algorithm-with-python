# BOJ 17472
import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
map_input = []
land = 7

# 입력으로 주어진 지도 초기화
for _ in range(N):
    line = list(map(int, input().split()))
    for i in range(M):
        if line[i] == 1:
            line[i] = land
    map_input.append(line)

diff = [(-1, 0), (0, -1), (0, 1), (1, 0)]


# 각 섬에 번호 매기기
def mark_land(i, j, land_num):
    que = deque()
    que.append((i, j))

    while que:
        now_x, now_y = que.popleft()
        map_input[now_x][now_y] = land_num

        for diff_x, diff_y in diff:
            next_x = now_x + diff_x
            next_y = now_y + diff_y

            if next_x >= N or next_x < 0:
                continue
            if next_y >= M or next_y < 0:
                continue

            if map_input[next_x][next_y] == land:
                que.append((next_x, next_y))


land_num = 0
for i in range(N):
    for j in range(M):
        if map_input[i][j] == land:
            land_num += 1
            mark_land(i, j, land_num)

edge_list = []
heapq.heapify(edge_list)


# 에지 리스트 초기화
def find_edge(i, j):
    up = 0
    down = 0
    right = 0
    left = 0

    for y in range(j + 1, M):
        if map_input[i][y] != 0:
            break
        right += 1

        # 지도의 끝까지 섬을 만나지 못했을 경우
        if y + 1 == M:
            right = 0

    for y in range(j - 1, -1, -1):
        if map_input[i][y] != 0:
            break
        left += 1

        # 지도의 끝까지 섬을 만나지 못했을 경우
        if y - 1 == -1:
            left = 0

    for x in range(i + 1, N):
        if map_input[x][j] != 0:
            break
        down += 1

        # 지도의 끝까지 섬을 만나지 못했을 경우
        if x + 1 == N:
            down = 0

    for x in range(i - 1, -1, -1):
        if map_input[x][j] != 0:
            break
        up += 1

        # 지도의 끝까지 섬을 만나지 못했을 경우
        if x - 1 == -1:
            up = 0

    return up, down, right, left


for i in range(N):
    for j in range(M):
        if map_input[i][j] != 0:
            start_land = map_input[i][j]
            up, down, right, left = find_edge(i, j)

            if up > 1:
                end_land = map_input[i - up - 1][j]
                heapq.heappush(edge_list, (up, start_land, end_land))

            if down > 1:
                end_land = map_input[i + down + 1][j]
                heapq.heappush(edge_list, (down, start_land, end_land))

            if right > 1:
                end_land = map_input[i][j + right + 1]
                heapq.heappush(edge_list, (right, start_land, end_land))

            if left > 1:
                end_land = map_input[i][j - left - 1]
                heapq.heappush(edge_list, (left, start_land, end_land))

# 최소 신장 트리를 이용하여 답 구하기
node = [i for i in range(land_num + 1)]


def find(e):
    if node[e] == e:
        return node[e]

    root = find(node[e])
    node[e] = root
    return root


def union(a, b):
    if node[a] != a:
        a = find(a)
    if node[b] != b:
        b = find(b)

    if a != b:
        node[a] = b


# 최소 신장 트리에 포함된 섬의 수
included_land = 0
answer = 0
while included_land < land_num - 1:
    # 모든 섬을 연결하지 못하는 경우 대비
    if not edge_list:
        break

    w, s, e = heapq.heappop(edge_list)
    if find(s) != find(e):
        answer += w
        union(s, e)
        included_land += 1


if included_land == land_num - 1:
    print(answer)
else:
    print(-1)
