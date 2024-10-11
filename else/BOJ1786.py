S = input()
P = input()
str_len = len(S)
pattern_len = len(P)
table = [0] * pattern_len

j = 0
for i in range(1, pattern_len):
    while j > 0 and P[j] != P[i]:
        j = table[j - 1]

    if P[j] == P[i]:
        j += 1
        table[i] = j

j = 0
cnt = 0
position = []

for i in range(str_len):
    while j > 0 and S[i] != P[j]:
        j = table[j - 1]
    if S[i] == P[j]:
        if j == pattern_len - 1:
            cnt += 1
            position.append(i - pattern_len + 2)
            j = table[j]
        else:
            j += 1

print(cnt)
if cnt != 0:
    print(*position)