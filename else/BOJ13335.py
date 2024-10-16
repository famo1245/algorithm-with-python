import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
a = list(map(int, input().split()))
sum_now = 0
time = 0
index = 0
count = 0
q = deque(maxlen=w)

for _ in range(w):
    q.append(0)

while True:
    weight = q.popleft()
    time += 1
    if weight != 0:
        count += 1
    if count == n:
        break

    sum_now -= weight
    if index < n and sum_now + a[index] <= L:
        q.append(a[index])
        sum_now += a[index]
        index += 1
    else:
        q.append(0)

print(time)
