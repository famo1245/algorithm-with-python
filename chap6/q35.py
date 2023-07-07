# BOJ 1931
N = int(input())
time_table = [[0] * 2 for _ in range(N)]

for i in range(N):
    start, end = map(int, input().split())
    time_table[i][0] = end
    time_table[i][1] = start

time_table.sort()
count = 0
end = -1

for i in range(N):
    if time_table[i][1] >= end:
        end = time_table[i][0]
        count += 1

print(count)
