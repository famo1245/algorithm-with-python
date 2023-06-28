import sys
import math
sys.setrecursionlimit(10 ** 6)

N = int(input())


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def dfs(n):
    if len(str(n)) == N:
        print(n)
    else:
        for i in range(1, 10, 2):
            num = n * 10 + i
            if is_prime(num):
                dfs(num)


dfs(2)
dfs(3)
dfs(5)
dfs(7)
