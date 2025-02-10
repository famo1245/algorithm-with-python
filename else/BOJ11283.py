# BOJ 11283
import sys
input = sys.stdin.readline

base = ord('가')
char = ord(input().strip())
answer = char - base + 1
print(answer)
