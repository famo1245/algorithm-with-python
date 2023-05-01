n = int(input())
numbers = list(input())
sum = 0
if len(numbers) != n:
    print("입력 받은 숫자 개수 다름")
    print(len(numbers))

else:
    for i in numbers:
        sum += int(i)
    print(sum)
