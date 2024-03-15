# BOJ 21568
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


A, B, C = map(int, input().split())


def Execute(a, b):
    ret = [0] * 2
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a // b
    v = Execute(b, a % b)
    ret[0] = v[1]
    ret[1] = v[0] - v[1] * q
    return ret


mgcd = gcd(A, B)
if C % mgcd != 0:
    print(-1)
else:
    share = int(C / mgcd)
    remain = Execute(A, B)
    print(remain[0] * share, end='')
    print(remain[1] * share)
