import sys
import heapq
input = sys.stdin.readline

q = int(input())
left = []
right = []
offset = left_sum = right_sum = 0
left_cnt = right_cnt = 0

for _ in range(q):
    command, *param = map(int, input().split())

    if command == 1:
        x, y = param
        offset += y

        if (left and -left[0] >= x) or (right and right[0] > x):
            heapq.heappush(left, -x)
            left_sum += x
            left_cnt += 1
        else:
            heapq.heappush(right, x)
            right_sum += x
            right_cnt += 1

        if left_cnt < right_cnt:
            value = heapq.heappop(right)
            heapq.heappush(left, -value)
            right_sum -= value
            right_cnt -= 1
            left_sum += value
            left_cnt += 1
        elif left_cnt > right_cnt + 1:
            value = -heapq.heappop(left)
            heapq.heappush(right, value)
            right_sum += value
            right_cnt += 1
            left_sum -= value
            left_cnt -= 1

    else:
        count = left_cnt + right_cnt
        result = 0
        if count % 2 == 1:
            result = -left[0]
        print(-left[0], right_sum - left_sum + result + offset)
