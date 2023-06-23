import sys

input = sys.stdin.readline
count = 0


def merge_sort(s, e):
    global count

    if e - s < 1:
        return

    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)

# 나중에 풀어보기
