N = int(input())
string = input()
D = [0] * (N + 8)
D[N] = 1

for i in range(N - 1, -1, -1):
    if string[i:i + 8] == "longlong":
        D[i] = D[i + 1] + D[i + 8]
    else:
        D[i] = D[i + 1]

print(D[0])
