# N = input()
# A = []
#
# for i in range(len(N)):
#     A.append(int(N[i]))
#
# A.sort(reverse=True)
#
# for i in range(len(A)):
#     print(A[i], end='')

# list 함수를 사용 하면 알아서 파싱 해줌
# 출력 하므로 굳이 정수형 변환 필요 x

A = list(input())

A.sort(reverse=True)

for i in range(len(A)):
    print(A[i], end='')
