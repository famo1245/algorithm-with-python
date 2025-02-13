# BOJ 1202
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
stones = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
stones.sort()
bags.sort()

answer = 0
temp = []
index = 0

for bag in bags:
    while index < N and stones[index][0] <= bag:
        heapq.heappush(temp, -stones[index][1])
        index += 1

    if temp:
        answer -= heapq.heappop(temp)

print(answer)
