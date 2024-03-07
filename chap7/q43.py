# BOJ 1850
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


A, B = map(int, input().split())

if A > B:
    result = gcd(A, B)
else:
    result = gcd(B, A)

for i in range(result):
    print(1, end='')
