# BOJ 1722
from math import factorial
N = int(input())
line = list(map(int, input().split()))
num_list = [str(i) for i in range(N + 1)]

find_index = -1
find_num = -1
if line[0] == 1:
    find_index = line[1]
else:
    find_num = ''
    for i in range(1, len(line)):
        find_num += str(line[i])
    find_num = int(find_num)

count = 0
possible = factorial(N - 1)
i = 1
while i < N + 1:
    num = str(num_list[i])
    used = [False] * (N + 1)
    j = (i + 1) % (N + 1)
    while len(num) < N + 1:
        if not used[j]:
            num += str(num_list[j])
        j = (j + 1) % (N + 1)

    count += 1
    if count == find_index:
        print()
    if find_num == int(num):
        print(count)

    if count % possible == 0:
        continue
    i += 1
