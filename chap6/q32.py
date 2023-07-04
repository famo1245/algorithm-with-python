N, K = map(int, input().split())

A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0
idx = N - 1

while K != 0:
    count += K // A[idx]
    K %= A[idx]
    idx -= 1

print(count)
