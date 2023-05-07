import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
G = list(map(int, input().split()))
G.sort()

start_idx = 1
end_idx = 1
count = 1
sum = 1

# while end_idx != N: