import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

min_sum = 9876543210
answer = []
for i in range(N):
    start = i + 1
    end = N - 1

    while start < N and start != end:
        sum_now = solutions[i] + solutions[start] + solutions[end]
        if sum_now == 0:
            print(solutions[i], solutions[start], solutions[end])
            exit(0)

        if min_sum >= abs(sum_now):
            if min_sum > abs(sum_now):
                min_sum = abs(sum_now)
                answer.clear()
            answer.append([solutions[i], solutions[start], solutions[end]])

        if sum_now > 0:
            end -= 1
        else:
            start += 1

print(*answer[0])
