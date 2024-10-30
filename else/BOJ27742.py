import sys
input = sys.stdin.readline

T, K = map(int, input().split())
T -= 1
scores = [list(map(int, input().split())) for _ in range(4)]
result = [[i, 0, 0, 0] for i in range(4)]

for i in range(4):
    for j in range(4):
        if i == j:
            continue

        my = scores[i][j]
        opponent = scores[j][i]

        if my != -1:
            if my > opponent:
                result[i][1] += 3
            elif my == scores[j][i]:
                result[i][1] += 1

            result[i][2] += my - opponent
            result[i][3] += my
        else:
            result[i][2] -= opponent

result.sort(key=lambda x: (-x[1], -x[2], -x[3], -x[0]))

min_score = K + 1
for rank in range(4):
    if result[rank][0] == T:
        if rank < 2:
            min_score = 0
            break

print(result)
if min_score > K:
    print(-1)
else:
    print(min_score)
