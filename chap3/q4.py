import sys
input = sys.stdin.readline
n = int(input())
A = [[0] * (n+1)]
D = [[0] * (n+1)] * (n+1)

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

print(A)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

print(D)
#
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     answer = D[x2][y2] - (D[x1-1][y2] + D[x2][y1-1] + D[x1-1][y1-1])
#     print(answer)
