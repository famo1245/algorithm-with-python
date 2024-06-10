# BOJ 1722
from math import factorial
N = int(input())
line = list(map(int, input().split()))
num_list = [i for i in range(1, N + 1)]
events = [factorial(N - i) for i in range(N)]


def find_index(index):
    used = [False] * (N + 1)
    result = []
    digit = N - 1
    while index > events[digit]:
        digit -= 1

    for i in range(digit + 1):
        result.append(num_list[i])
        used[num_list[i]] = True

    return result


if line[0] == 1:
    result = find_index(line[1])

else:
    find_num = ''
    for i in range(1, len(line)):
        find_num += str(line[i])
    find_num = int(find_num)

print(*result)