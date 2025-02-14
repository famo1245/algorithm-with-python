# BOJ 2166
import sys
input = sys.stdin.readline

N = int(input())
x = []
y = []

for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

sum_a = 0
sum_b = 0
for i in range(N):
    sum_a += x[i] * y[(i + 1) % N]
    sum_b += x[(i + 1) % N] * y[i]

result = 0.5 * abs(sum_a - sum_b)
print(round(result, 2))
