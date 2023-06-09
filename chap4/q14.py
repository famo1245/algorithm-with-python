N = int(input())
A = [0] * N
A.sort()

for i in A:
    print(i)

# 수가 최대 1000까지 이므로 버블 정렬 사용
# for i in range(N-1):
#     for j in range(N-1-i):
#         if A[j] > A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]


