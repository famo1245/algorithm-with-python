# BOJ 10844
N = int(input())
MAX = 100
NUM_RANGE = 10
DIVISOR = 1000000000
# D[n][h] => 길이가 n일때 숫자 h로 끝나는 계단의 수
D = [[0] * NUM_RANGE for _ in range(MAX + 1)]

# init DP table, 한 자리수일 때 0으로 시작할 수 없으므로 D[1][0] == 0
for i in range(1, NUM_RANGE):
    D[1][i] = 1

# D[i][h] = D[i - 1][h + 1] in h == 0
# D[i][h] = D[i - 1][h - 1] in h == 9
# D[i][h[ = D[i - 1][h - 1] + D[i - 1][h + 1]
# fill data
for i in range(2, MAX + 1):
    for h in range(NUM_RANGE):
        if h == 0:
            D[i][h] = D[i - 1][h + 1]
        elif h == 9:
            D[i][h] = D[i - 1][h - 1]
        else:
            D[i][h] = D[i - 1][h - 1] + D[i - 1][h + 1]

print(sum(D[N]) % DIVISOR)
