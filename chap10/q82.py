# BOJ 1256
import sys

input = sys.stdin.readline
# N -> a의 개수, M -> z의 개수, K번째 문자열
N, M, K = map(int, input().split())
D = [[0 for _ in range(M + N + 1)] for _ in range(M + N + 1)]

# init DP table
for i in range(M + N + 1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(1, M + N + 1):
    for j in range(1, i + 1):
        D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

# K가 사전에 수록되어 있는 문자열 개수보다 많은 경우
if K > D[N + M][M]:
    print(-1)
    exit(0)

while N != 0 or M != 0:
    total = M + N - 1
    # 현재 단계에서 a를 선택했을 때 남은 문자로 만들 수 있는 경우의 수
    remain_case = D[total][M]
    # 남은 경우의 수가 더 클 때 -> a 선택
    if remain_case >= K:
        print('a', end='')
        N -= 1
    else:
        print('z', end='')
        K -= remain_case
        M -= 1
