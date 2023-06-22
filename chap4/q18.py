N = int(input())
P = list(map(int, input().split()))

P.sort()

T = []
T.append(P[0])

for i in range(1, N):
    T.append(P[i] + T[i-1])

print(sum(T))
