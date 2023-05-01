n = int(input())
scores = list(map(int, input().split()))

if len(scores) != n:
    print('입력한 과목의 수와 다릅니다')

else:
    M = max(scores)
    print(sum(scores) / M * 100 / n)
