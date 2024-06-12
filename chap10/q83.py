# BOJ 1947
N = int(input())
MAX = 1000000
DIVISOR = 1000000000
D = [0] * (MAX + 1)

# init DP table
D[0] = -1
D[1] = 0
D[2] = 1

for i in range(3, MAX + 1):
    D[i] = (i - 1) * (D[i - 2] + D[i - 1]) % DIVISOR

print(D[N])
