# BOJ 1934
# 최소공배수 = 최대공약수 * a * b

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


T = int(input())

for i in range(T):
    A, B = map(int, input().split())

    if A > B:
        result = gcd(A, B)
    else:
        result = gcd(B, A)

    print(int(A * B / result))
