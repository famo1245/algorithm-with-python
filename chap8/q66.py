# BOJ 1414
import sys
import heapq
input = sys.stdin.readline

N = int(input())
total_lengths = 0
edge_list = []
heapq.heapify(edge_list)


# 알파벳을 숫자로
def convert(e):
    if e == '0':
        return 0

    # 문자의 유니코드 정수값을 반환하는 ord함수 이용
    diff = ord(e) - ord('a')
    # 소문자인 경우
    if diff >= 0:
        return diff + 1
    # 대문자인 경우
    return diff + 59


for i in range(1, N + 1):
    temp = list(input().strip())
    line = list(map(convert, temp))

    for j in range(N):
        total_lengths += line[j]
        if line[j] == 0:
            continue
        heapq.heappush(edge_list, (line[j], i, j + 1))

computers = [i for i in range(N + 1)]


def find(e):
    if computers[e] == e:
        return computers[e]
    root = find(computers[e])
    computers[e] = root
    return root


def union(a, b):
    if computers[a] != a:
        a = find(computers[a])
    if computers[b] != b:
        b = find(computers[b])

    if a != b:
        computers[a] = b


included_computers = 0
answer = 0
while included_computers < N - 1:
    # 연결할 수 없는 컴퓨터가 있는 경우
    if not edge_list:
        break

    w, s, e = heapq.heappop(edge_list)
    if find(s) != find(e):
        answer += w
        included_computers += 1
        union(s, e)

if included_computers == N - 1:
    print(total_lengths - answer)
else:
    print(-1)
