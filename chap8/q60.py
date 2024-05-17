# BOJ 1219
# gg 의 경우 잘못 설정
# import sys
# import math
# input = sys.stdin.readline
#
# N, start, end, M = map(int, input().split())
# routes = []
# balances = [-math.inf] * N
# balances[start] = 0
#
# for _ in range(M):
#     s, e, w = map(int, input().split())
#     routes.append((s, e, -w))
#
# incomes = list(map(int, input().split()))
#
# for _ in range(N):
#     for s, e, w in routes:
#         if balances[s] != -math.inf and balances[e] < balances[s] + w + incomes[e]:
#             balances[e] = balances[s] + w + incomes[s]
#
# has_cycle = False
#
# for s, e, w in routes:
#     if balances[s] != -math.inf and balances[e] < balances[s] + w + incomes[e]:
#         has_cycle = True
#
#
# if has_cycle:
#     print('Gee')
#     exit(0)
#
# if balances[end] == -math.inf:
#     print('gg')
# else:
#     print(balances[end])

# 출발도시 == 도착도시인 경우 도시에서 벌 수 있는 돈이 있음에도 0원
# import sys
# import math
# input = sys.stdin.readline
#
# N, start, end, M = map(int, input().split())
# routes = []
# balances = [-math.inf] * N
# balances[start] = 0
#
# for _ in range(M):
#     s, e, w = map(int, input().split())
#     routes.append((s, e, -w))
#
# incomes = list(map(int, input().split()))
#
# for _ in range(N):
#     for s, e, w in routes:
#         if balances[s] != -math.inf and balances[e] < balances[s] + w + incomes[e]:
#             balances[e] = balances[s] + w + incomes[s]
#
# has_cycle = False
#
# for s, e, w in routes:
#     if balances[s] != -math.inf and balances[e] < balances[s] + w + incomes[e]:
#         has_cycle = True
#
# if balances[end] == -math.inf:
#     print('gg')
#     exit(0)
#
# if has_cycle:
#     print('Gee')
# else:
#     print(balances[end])

# 사이클 내에 도착도시가 있으면 안됨
# import sys
# import math
# input = sys.stdin.readline
#
# N, start, end, M = map(int, input().split())
# routes = []
# balances = [-math.inf] * N
#
# for _ in range(M):
#     s, e, w = map(int, input().split())
#     routes.append((s, e, -w))
#
# incomes = list(map(int, input().split()))
# balances[start] = incomes[start]
#
# for _ in range(N):
#     for s, e, w in routes:
#         if balances[s] != -math.inf and balances[e] < balances[s] + w + incomes[e]:
#             balances[e] = balances[s] + w + incomes[s]
#
# has_cycle = False
#
# # 이 부분에서 변경이 발생 안해서 사이클 중간 값 갱신x
# for s, e, w in routes:
#     if balances[s] != -math.inf and balances[e] < balances[s] + w + incomes[e]:
#         has_cycle = True
#
# if balances[end] == -math.inf:
#     print('gg')
#     exit(0)
#
# if has_cycle:
#     print('Gee')
# else:
#     print(balances[end])

# import sys
# import math
# input = sys.stdin.readline
#
# N, start, end, M = map(int, input().split())
# routes = []
# balances = [-math.inf] * N
#
# for _ in range(M):
#     s, e, w = map(int, input().split())
#     routes.append((s, e, -w))
#
# incomes = list(map(int, input().split()))
# balances[start] = incomes[start]
#
# for _ in range(N):
#     for s, e, w in routes:
#         if balances[s] != -math.inf and balances[e] < balances[s] + w + incomes[e]:
#             balances[e] = balances[s] + w + incomes[e]
# # 변경
# temp_balance = balances[end]
#
# # 도착 도시와 관련된 사이클만 취급
# for s, e, w in routes:
#     if balances[s] != -math.inf and balances[e] < balances[s] + w + incomes[e]:
#         balances[e] = balances[s] + w + incomes[e]
#
# if balances[end] == -math.inf:
#     print('gg')
#     exit(0)
#
# if temp_balance != balances[end]:
#     print('Gee')
# else:
#     print(balances[end])

import sys
import math
input = sys.stdin.readline

N, start, end, M = map(int, input().split())
routes = []
balances = [-math.inf] * N

for _ in range(M):
    s, e, w = map(int, input().split())
    routes.append((s, e, -w))

incomes = list(map(int, input().split()))
balances[start] = incomes[start]

for i in range(N + 101):
    for s, e, w in routes:
        if balances[s] == -math.inf:
            continue
        elif balances[s] == math.inf:
            balances[e] = math.inf
        elif balances[e] < balances[s] + w + incomes[e]:
            balances[e] = balances[s] + w + incomes[e]
            if i >= N - 1:
                balances[e] = math.inf

if balances[end] == -math.inf:
    print('gg')
elif balances[end] == math.inf:
    print('Gee')
else:
    print(balances[end])

# 도착과 관련 없는 사이클
# 5 0 4 5
# 0 1 0
# 1 2 0
# 2 3 0
# 3 1 0
# 0 4 0
# 1 1 1 1 1
# 2

# 사이클 중간
# 5 0 3 5
# 0 1 0
# 1 2 0
# 2 3 0
# 3 1 0
# 0 4 0
# 1 1 1 1 1
# Gee

# 사이클을 계속 돌면서 업데이트가 안되는 경우