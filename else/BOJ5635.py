# BOJ 5635
import sys
input = sys.stdin.readline

N = int(input())
l = []

for _ in range(N):
    name, *birth = input().split()
    date, month, year = map(int, birth)
    l.append((year, month, date, name))

l.sort()
print(l[N - 1][3], l[0][3], sep="\n")
