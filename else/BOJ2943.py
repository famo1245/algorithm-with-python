import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
bucket_size = int(math.sqrt(n))
boxes = [0] * n
buckets = [0] * (n // bucket_size + 1)

for _ in range(m):
    count, pos = map(int, input().split())
    start = pos - 1
    end = start + count
    total_matches = 0

    while start < end and start % bucket_size != 0:
        boxes[start] += 1
        total_matches += boxes[start]
        start += 1

    if end != n:
        while start < end and end % bucket_size != 0:
            end -= 1
            boxes[end] += 1
            total_matches += boxes[end]

    while start < end:
        bucket_idx = start // bucket_size
        buckets[bucket_idx] += 1
        total_matches += buckets[bucket_idx]
        start += bucket_size

    print(total_matches)
