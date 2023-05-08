# 시간 제한 2초
import sys
import time

start_time = time.time()
input = sys.stdin.readline

S, P = map(int, input().split())
char_list = list(input())
check = list(map(int, input().split()))
answer = 0

for i in range(S-P+1):
    flag = 1
    end = i + P
    count = [0] * 4

    for j in range(i, end):
        if char_list[j] == 'A':
            count[0] += 1
        elif char_list[j] == 'C':
            count[1] += 1
        elif char_list[j] == 'G':
            count[2] += 1
        elif char_list[j] == 'T':
            count[3] += 1

    for j in range(4):
        if check[j] > count[j]:
            flag = 0
            break

    if flag == 1:
        answer += 1

print(answer)
print(time.time() - start_time)
# 실행 시간 초과
