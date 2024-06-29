# SW Academy D2 12712
T = int(input())


def catch_max_flies(row, col):
    result_plus = flies[row][col]
    result_x = flies[row][col]

    # + => |
    for dr in range(len(dx)):
        r = row + dx[dr]
        if -1 < r < N:
            result_plus += flies[r][col]
    # + => -
    for dc in range(len(dy)):
        c = col + dy[dc]
        if -1 < c < N:
            result_plus += flies[row][c]

    # x => \
    for d in range(len(dx)):
        r = row + dx[d]
        c = col + dy[d]
        if -1 < r < N and -1 < c < N:
            result_x += flies[r][c]

    # x => /
    for d in range(len(dx)):
        r = row + dx[d]
        c = col + dy[len(dy) - d - 1]
        if -1 < r < N and -1 < c < N:
            result_x += flies[r][c]

    return max(result_x, result_plus)


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flies = []
    D = [[0] * N for _ in range(N)]

    dx = []
    for i in range(-M + 1, M):
        if i != 0:
            dx.append(i)
    dy = dx.copy()

    for _ in range(N):
        line = list(map(int, input().split()))
        flies.append(line)

    for i in range(N):
        for j in range(N):
            result = catch_max_flies(i, j)

            if i == 0 and j == 0:
                D[i][j] = result
            elif j == 0:
                D[i][j] = max(result, D[i - 1][N - 1])
            else:
                D[i][j] = max(result, D[i][j - 1])

    print(f'#{test_case} {D[N - 1][N - 1]}')
