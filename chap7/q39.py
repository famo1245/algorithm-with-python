# BOJ 1747
import math

N = int(input())
A = [0] * 10000001

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):
        A[j] = 0


def isPalindrome(target):
    temp = list(str(target))
    s = 0
    e = len(temp) - 1
    while s < e:
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True


i = N

while True:
    if i == len(A):
        break
    if A[i] != 0:
        result = A[i]

        if isPalindrome(result):
            print(result)
            break
    i += 1

# for i in range(N, len(A)):
#     if A[i] == 0:
#         continue
#
#     temp = str(A[i])
#
#     # 소수가 한자리 수인 경우 -> 무조건 회문
#     if len(temp) == 1:
#         print('line 1')
#         print(A[i])
#         break
#
#     max = len(temp) - 1
#     min = 0
#     arr = list(map(int, temp))
#     flag = 1
#
#     while min <= max:
#         if arr[max] != arr[min]:
#             flag = 0
#             break
#
#         max -= 1
#         min += 1
#
#     if flag:
#         print(A[i])
#         break
