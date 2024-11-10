import sys
input = sys.stdin.readline

Q = int(input())
info = {}
result = 0

for _ in range(Q):
    line = input().split()

    if int(line[0]) == 1:
        name = line[1]
        information = list(map(int, line[3:]))
        if name in info:
            info[name].extend(information)
        else:
            info[name] = information
    else:
        name = line[1]
        if name in info:
            info[name].sort(reverse=True)
            for _ in range(min(int(line[2]), len(info[name]))):
                result += info[name].pop(0)

print(result)

# heapq보다 sort가 더 빠르더라 => 다 뽑아내는 경우 때문인가
# import sys
# import heapq
# input = sys.stdin.readline
#
#
# def convert(e):
#     return -int(e)
#
#
# Q = int(input())
# info = {}
# result = 0
#
# for _ in range(Q):
#     line = input().split()
#
#     if int(line[0]) == 1:
#         name = line[1]
#         information = list(map(convert, line[3:]))
#         if name in info:
#             for i in information:
#                 heapq.heappush(info[name], i)
#         else:
#             info[name] = information
#     else:
#         name = line[1]
#         if name in info:
#             for _ in range(min(int(line[2]), len(info[name]))):
#                 result += abs(heapq.heappop(info[name]))
#
# print(result)