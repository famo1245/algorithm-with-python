from queue import PriorityQueue
import sys

input = sys.stdin.readline
#print = sys.stdout.write   # 한줄 씩 출력

N = int(input())
my_queue = PriorityQueue()

for _ in range(N):
    x = int(input())
    if x == 0:
        if my_queue.empty():
            print('0')
        else:
            result = my_queue.get()
            print(result[1])
    else:
        my_queue.put((abs(x), x))
