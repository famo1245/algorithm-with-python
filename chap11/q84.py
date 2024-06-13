# BOJ 1463
from math import inf
N = int(input())
MAX = 1000000
D = [0] * (MAX + 1)

# init DP table
D[2] = 1
D[3] = 1

for i in range(4, MAX + 1):
    case1, case2, case3 = inf, inf, inf

    if i % 3 == 0:
        case1 = D[i // 3]
    if i % 2 == 0:
        case2 = D[i // 2]
    case3 = D[i - 1]
    # 최솟값 찾기
    D[i] = min(case1, case2, case3) + 1

print(D[N])
