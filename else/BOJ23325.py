from math import inf

operation = list(input())
total_length = len(operation)
D = [-inf] * total_length

if total_length == 1:
    if operation[0] == '+':
        print(10)
    else:
        print(1)
    exit(0)

if operation[0] == '-':
    D[0] = 1
else:
    D[0] = 10
    if operation[1] == '-':
        D[1] = 11

for i in range(2, total_length):
    if operation[i] == '+':
        if operation[i - 1] == '-':
            D[i] = D[i - 2] - 10
        else:
            D[i] = D[i - 2] + 10
    else:
        if operation[i - 1] == '-':
            D[i] = D[i - 2] - 1
        else:
            if i >= 3:
                if operation[i - 2] == '-':
                    D[i] = max(D[i - 2] + 1, D[i - 3] - 11)
                else:
                    D[i] = max(D[i - 2] + 1, D[i - 3] + 11)
            else:
                D[i] = D[i - 2] + 1

print(D[total_length - 1])
