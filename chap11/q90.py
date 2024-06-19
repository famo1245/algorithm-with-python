# BOJ 9252
import sys

input = sys.stdin.readline
string_input1 = list(input().strip())
string_input2 = list(input().strip())

FIRST_INPUT_LENGTH = len(string_input1)
SECOND_INPUT_LENGTH = len(string_input2)
D_length = [[0] * FIRST_INPUT_LENGTH for _ in range(SECOND_INPUT_LENGTH)]
D_lcs = [[''] * FIRST_INPUT_LENGTH for _ in range(SECOND_INPUT_LENGTH)]

# init DP table
if string_input1[0] == string_input2[0]:
    D_length[0][0] = 1
    D_lcs[0][0] = string_input1[0]
for i in range(1, FIRST_INPUT_LENGTH):
    if string_input1[i] == string_input2[0]:
        D_length[0][i] = 1
        D_lcs[0][i] = string_input1[i]
    else:
        D_length[0][i] = D_length[0][i - 1]
        D_lcs[0][i] = D_lcs[0][i - 1]

for j in range(1, SECOND_INPUT_LENGTH):
    if string_input1[0] == string_input2[j]:
        D_length[j][0] = 1
        D_lcs[j][0] = string_input2[j]
    else:
        D_length[j][0] = D_length[j - 1][0]
        D_lcs[j][0] = D_lcs[j - 1][0]

for i in range(1, SECOND_INPUT_LENGTH):
    for j in range(1, FIRST_INPUT_LENGTH):
        if string_input1[j] == string_input2[i]:
            D_length[i][j] = D_length[i - 1][j - 1] + 1
            D_lcs[i][j] = D_lcs[i - 1][j - 1] + string_input1[j]
        else:
            if D_length[i - 1][j] < D_length[i][j - 1]:
                D_length[i][j] = D_length[i][j - 1]
                D_lcs[i][j] = D_lcs[i][j - 1]
            else:
                D_length[i][j] = D_length[i - 1][j]
                D_lcs[i][j] = D_lcs[i - 1][j]

print(D_length[SECOND_INPUT_LENGTH - 1][FIRST_INPUT_LENGTH - 1])
if D_length[SECOND_INPUT_LENGTH - 1][FIRST_INPUT_LENGTH - 1] != 0:
    print(D_lcs[SECOND_INPUT_LENGTH - 1][FIRST_INPUT_LENGTH - 1])
