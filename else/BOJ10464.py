# BOJ 10464
import sys
input = sys.stdin.readline

index = {}


def sequence_xor(num):
    div = num % 4
    if div == 1:
        return 1
    elif div == 2:
        return num + 1
    elif div == 3:
        return 0

    return num


for _ in range(int(input())):
    S, F = map(int, input().split())
    S -= 1

    if S not in index:
        index[S] = sequence_xor(S)

    if F not in index:
        index[F] = sequence_xor(F)

    print(index[S] ^ index[F])
