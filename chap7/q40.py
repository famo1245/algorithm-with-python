# BOJ 1016
import math

min, max = map(int, input().split())
A = [1] * (max - min + 1)

for i in range(2, int(math.sqrt(max) + 1)):
    power = i * i
    start = int(min/power)

    if min % power != 0:
        start += 1

    for j in range(start, int(max/power) + 1):
        A[int((j * power) - min)] = 0

count = 0

for i in range(0, max - min + 1):
    if A[i]:
        count += 1

print(count)
