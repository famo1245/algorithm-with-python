import math

N = int(input())
if N == 1:
    print(0)
    exit(0)

num_list = [0] * (N + 1)

for i in range(2, N + 1):
    num_list[i] = i

for i in range(2, int(math.sqrt(N)) + 1):
    if num_list[i] == 0:
        continue
    else:
        for j in range(i + i, N + 1, i):
            num_list[j] = 0

prime = []
for i in range(2, N + 1):
    if num_list[i] != 0:
        prime.append(i)

size = len(prime)
start = end = 0
sumNums = prime[start]
result = 0
while start <= end:
    if sumNums < N:
        end += 1
        if end >= size:
            break

        sumNums += prime[end]
    elif sumNums > N:
        sumNums -= prime[start]
        start += 1
    else:
        sumNums -= prime[start]
        start += 1
        result += 1

print(result)
