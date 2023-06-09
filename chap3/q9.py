# 시간 제한 2초
import sys

input = sys.stdin.readline
checkList = [0] * 4
myList = [0] * 4
checkValid = 0


def addlist(c):
    global checkValid, checkList, myList
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkValid += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkValid += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkValid += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkValid += 1


def removelist(c):
    global checkValid, checkList, myList
    if c == 'A':
        if myList[0] == checkList[0]:
            checkValid -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkValid -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkValid -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkValid -= 1
        myList[3] -= 1


S, P = map(int, input().split())
char_list = list(input())
checkList = list(map(int, input().split()))
answer = 0

for i in range(4):
    if checkList[i] == 0:
        checkValid += 1

for i in range(P):
    addlist(char_list[i])

if checkValid == 4:
    answer += 1

for i in range(P, S):
    remove_idx = i - P
    addlist(char_list[i])
    removelist(char_list[remove_idx])
    if checkValid == 4:
        answer += 1

print(answer)

# 내 풀이: 시간 초과
# for i in range(S-P+1):
#     flag = 1
#     end = i + P
#     count = [0] * 4
#
#     for j in range(i, end):
#         if char_list[j] == 'A':
#             count[0] += 1
#         elif char_list[j] == 'C':
#             count[1] += 1
#         elif char_list[j] == 'G':
#             count[2] += 1
#         elif char_list[j] == 'T':
#             count[3] += 1
#
#     for j in range(4):
#         if check[j] > count[j]:
#             flag = 0
#             break
#
#     if flag == 1:
#         answer += 1
