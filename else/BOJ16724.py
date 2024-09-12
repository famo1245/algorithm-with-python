import sys
# for pypy3
# sys.setrecursionlimit(10 ** 4)
# for python3
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

MOVE = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

N, M = map(int, input().split())
map_input = [list(input().rstrip()) for i in range(N)]

visited = [[False] * M for _ in range(N)]
parents = [i for i in range(N * M)]


def find(a):
    if a == parents[a]:
        return a

    root = find(parents[a])
    parents[a] = root
    return root


def union(a, b):
    if a != parents[a]:
        a = find(parents[a])

    if b != parents[b]:
        b = find(parents[b])

    if a != b:
        parents[b] = a


def dfs(r, c):
    visited[r][c] = True
    nr = r + MOVE[map_input[r][c]][0]
    nc = c + MOVE[map_input[r][c]][1]
    union(r * M + c, nr * M + nc)

    if not visited[nr][nc]:
        dfs(nr, nc)


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)

s = set()
for i in range(N * M):
    s.add(find(parents[i]))

print(len(s))