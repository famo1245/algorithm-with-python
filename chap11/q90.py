# BOJ 9252
# python3 시간 초과
# import sys
#
# input = sys.stdin.readline
# string_input1 = list(input().strip())
# string_input2 = list(input().strip())
#
# FIRST_INPUT_LENGTH = len(string_input1)
# SECOND_INPUT_LENGTH = len(string_input2)
# D_length = [[0] * FIRST_INPUT_LENGTH for _ in range(SECOND_INPUT_LENGTH)]
# D_lcs = [[''] * FIRST_INPUT_LENGTH for _ in range(SECOND_INPUT_LENGTH)]
#
# # init DP table
# if string_input1[0] == string_input2[0]:
#     D_length[0][0] = 1
#     D_lcs[0][0] = string_input1[0]
# for i in range(1, FIRST_INPUT_LENGTH):
#     if string_input1[i] == string_input2[0]:
#         D_length[0][i] = 1
#         D_lcs[0][i] = string_input1[i]
#     else:
#         D_length[0][i] = D_length[0][i - 1]
#         D_lcs[0][i] = D_lcs[0][i - 1]
#
# for j in range(1, SECOND_INPUT_LENGTH):
#     if string_input1[0] == string_input2[j]:
#         D_length[j][0] = 1
#         D_lcs[j][0] = string_input2[j]
#     else:
#         D_length[j][0] = D_length[j - 1][0]
#         D_lcs[j][0] = D_lcs[j - 1][0]
#
# for i in range(1, SECOND_INPUT_LENGTH):
#     for j in range(1, FIRST_INPUT_LENGTH):
#         if string_input1[j] == string_input2[i]:
#             D_length[i][j] = D_length[i - 1][j - 1] + 1
#             D_lcs[i][j] = D_lcs[i - 1][j - 1] + string_input1[j]
#         else:
#             if D_length[i - 1][j] < D_length[i][j - 1]:
#                 D_length[i][j] = D_length[i][j - 1]
#                 D_lcs[i][j] = D_lcs[i][j - 1]
#             else:
#                 D_length[i][j] = D_length[i - 1][j]
#                 D_lcs[i][j] = D_lcs[i - 1][j]
#
# print(D_length[SECOND_INPUT_LENGTH - 1][FIRST_INPUT_LENGTH - 1])
# if D_length[SECOND_INPUT_LENGTH - 1][FIRST_INPUT_LENGTH - 1] != 0:
#     print(D_lcs[SECOND_INPUT_LENGTH - 1][FIRST_INPUT_LENGTH - 1])

# 시간 단축 -> lcs를 구하는 테이블 사용 빼고 분리
import sys

input = sys.stdin.readline
string_input1 = list(input().strip())
string_input2 = list(input().strip())

FIRST_INPUT_LENGTH = len(string_input1)
SECOND_INPUT_LENGTH = len(string_input2)
D_length = [[0] * FIRST_INPUT_LENGTH for _ in range(SECOND_INPUT_LENGTH)]

# init DP table
if string_input1[0] == string_input2[0]:
    D_length[0][0] = 1

for i in range(1, FIRST_INPUT_LENGTH):
    if string_input1[i] == string_input2[0]:
        D_length[0][i] = 1
    else:
        D_length[0][i] = D_length[0][i - 1]

for j in range(1, SECOND_INPUT_LENGTH):
    if string_input1[0] == string_input2[j]:
        D_length[j][0] = 1
    else:
        D_length[j][0] = D_length[j - 1][0]

for i in range(1, SECOND_INPUT_LENGTH):
    for j in range(1, FIRST_INPUT_LENGTH):
        if string_input1[j] == string_input2[i]:
            D_length[i][j] = D_length[i - 1][j - 1] + 1
        else:
            D_length[i][j] = max(D_length[i - 1][j], D_length[i][j - 1])

max_length = D_length[SECOND_INPUT_LENGTH - 1][FIRST_INPUT_LENGTH - 1]
print(max_length)
if max_length != 0:
    lcs = []
    i = SECOND_INPUT_LENGTH - 1
    j = FIRST_INPUT_LENGTH - 1

    while len(lcs) < max_length:
        if string_input1[j] == string_input2[i]:
            lcs.append(string_input2[i])
            i -= 1
            j -= 1
        else:
            if i == 0:
                j -= 1
            elif j == 0:
                i -= 1
            elif D_length[i - 1][j] < D_length[i][j - 1]:
                j -= 1
            else:
                i -= 1

    while lcs:
        print(lcs.pop(), end='')
