# BOJ 1541 중요한 알고리즘
A = list(map(str, input().split('-')))


def sum_element(s):
    temp_list = s.split('+')
    result = 0
    for j in range(len(temp_list)):
        result += int(temp_list[j])
    return result


answer = 0
for i in range(len(A)):
    temp = sum_element(A[i])

    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)
