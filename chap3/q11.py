# N = int(input())
# A = [0] * N
#
# for i in range(N):
#     A[i] = int(input())
#
#
# stack = []
# num = 1
# result = True
# answer = ""
#
# for i in range(N):
#     a = A[i]
#
#     if a >= num:
#         while a >= num:
#             stack.append(num)
#             num += 1
#             answer += "+\n"
#
#         stack.pop()
#         answer += "-\n"
#
#     else:
#         top = stack.pop()
#
#         if top > a:
#             result = False
#             print('NO')
#             break
#         else:
#             answer += "-\n"
#
# if result:
#     print(answer)

# 시간 초과

N = int(input())

num = 1
stack = []
answer = []
flag = True

for _ in range(N):
    n = int(input())

    while n >= num:
        stack.append(num)
        answer.append("+")
        num += 1

    if stack[-1] == n:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = False
        break

if flag:
    for i in answer:
       print(i)
