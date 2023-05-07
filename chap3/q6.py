n = int(input())

# 내 풀이, 메모리를 많이 소모한다
# N = [0] * (n+1)
# A = [0] * (n+1)
# count = 1 # 자기 자신
#
# for i in range(1, n):
#     N[i] = i
#     A[i] = A[i-1] + N[i]
#     if A[i] == n:
#         count += 1
#
# for i in range(1, n):
#     for j in range(i, n):
#         if A[j] - A[i] == n:
#             count += 1

# 교재 풀이, 투 포인터를 이용!
start_index = 1
end_index = 1
count = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index

    elif sum > n:
        sum -= start_index
        start_index += 1

    else:
        end_index += 1
        sum += end_index

print(count)
