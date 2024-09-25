import sys
input = sys.stdin.readline

N = int(input())
my_stack = list()

for _ in range(N):
    command = input().split()

    if command[0] == 'push':
        my_stack.append(command[1])
    elif command[0] == 'pop':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack.pop())
    elif command[0] == 'top':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack[-1])
    elif command[0] == 'size':
        print(len(my_stack))
    elif command[0] == 'empty':
        if len(my_stack) == 0:
            print(1)
        else:
            print(0)
