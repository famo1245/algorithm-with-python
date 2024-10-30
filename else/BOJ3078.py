import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
students = [input().rstrip() for _ in range(N)]

q = deque()
count = defaultdict(int)

answer = 0
for name in students:
    if count[len(name)] != 0:
        answer += count[len(name)]

    count[len(name)] += 1
    q.append(name)

    if len(q) == K + 1:
        popped = q.popleft()
        count[len(popped)] -= 1

print(answer)
