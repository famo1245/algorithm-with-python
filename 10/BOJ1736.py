# BOJ 1736
import sys
input = sys.stdin.readline

OFFSET = [(1, 0), (0, 1)]
N, M = map(int, input().split())
trash = 0
room = []

for i in range(N):
    temp = list(map(int, input().split()))

    for j in range(M):
        if temp[j]:
            trash += 1

    room.append(temp)

answer = 0
while trash:
    answer += 1
    start = 0
    for i in range(N):
        for j in range(start, M):
            if room[i][j]:
                room[i][j] = 0
                trash -= 1
                start = j

print(answer)
