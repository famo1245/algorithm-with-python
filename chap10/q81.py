# BOJ 1722
from math import factorial

N = int(input())
line = list(map(int, input().split()))
num_list = [i for i in range(1, N + 1)]
events = [factorial(N - i) for i in range(N)]


def find_by_index(index):
    result = []
    digit = 0

    while len(result) < N:
        count = 0
        while index > events[digit] * count:
            count += 1

        num = num_list.pop(count - 1)
        result.append(num)
        index = index - (events[digit] * (count - 1))
        digit += 1

    print(*result)


def find_by_num(num):
    result = 1
    for i in range(len(num)):
        if num[i] != num_list[0]:
            count = 0
            index = 0
            for j in range(len(num_list)):
                if num[i] > num_list[j]:
                    count += 1
                elif num_list[j] == num[i]:
                    index = j
                    break

            result += count + 1
            num_list.pop(index)
        else:
            num_list.pop(0)

    print(result)


if line[0] == 1:
    find_by_index(line[1])

else:
    find_num = line[1:]
    find_by_num(find_num)
