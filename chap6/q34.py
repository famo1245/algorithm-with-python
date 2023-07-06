# BOJ 1744
from queue import PriorityQueue

N = int(input())
plus_que = PriorityQueue()
minus_que = PriorityQueue()

zero_count = 0
one_count = 0

for _ in range(N):
    data = int(input())
    if data > 1:
        plus_que.put(data * -1)
    elif data == 1:
        one_count += 1
    elif data < 0:
        minus_que.put(data)
    else:
        zero_count += 1

sum = 0

while plus_que.qsize() > 1:
    num1 = plus_que.get() * -1
    num2 = plus_que.get() * -1

    sum += num1 * num2

if plus_que.qsize() > 0:
    sum += plus_que.get() * -1

while minus_que.qsize() > 1:
    num1 = minus_que.get()
    num2 = minus_que.get()

    sum += num1 * num2

if minus_que.qsize() > 0 and zero_count == 0:
    sum += minus_que.get()

sum += one_count

print(sum)
