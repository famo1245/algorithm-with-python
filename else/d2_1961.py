# SW Academy D2 1961
def rotate_table(t, n):
    rotate_90 = [[0] * n for _ in range(n)]
    rotate_180 = [[0] * n for _ in range(n)]
    rotate_270 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_90[i][j] = t[n - j - 1][i]
            rotate_180[i][j] = t[n - i - 1][n - j - 1]
            rotate_270[i][j] = t[j][n - i - 1]
    return [rotate_90, rotate_180, rotate_270]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    table = []

    for _ in range(N):
        line = input().split()
        table.append(line)

    degree_90, degree_180, degree_270 = rotate_table(table, N)

    print(f'#{test_case}')
    for i in range(N):
        print(''.join(degree_90[i]), ''.join(degree_180[i]), ''.join(degree_270[i]))
