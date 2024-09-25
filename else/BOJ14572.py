import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())

algo = [0 for i in range(K + 1)]
student_ability = []

for i in range(N):
    M, d = map(int, input().split())
    know = list(map(int, input().split()))
    student_ability.append([d, M, know])

student_ability.sort(key=lambda x: x[0])

start = end = 0
all_known_algo = sum_algo = 0
answer = -1
while True:
    if student_ability[end][0] - student_ability[start][0] > D:
        for num in student_ability[start][2]:
            algo[num] -= 1

            if algo[num] == 0:
                sum_algo -= 1

        start += 1

    if student_ability[end][0] - student_ability[start][0] <= D:
        all_known_algo = 0

        for num in student_ability[end][2]:
            algo[num] += 1

            if algo[num] == end - start + 1:
                all_known_algo += 1
            if algo[num] == 1:
                sum_algo += 1

        answer = max(answer, (sum_algo - all_known_algo) * (end - start + 1))
        end += 1

    if end == N:
        break

print(answer)