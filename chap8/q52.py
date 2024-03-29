import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = list(map(int, input().split()))
people = [i for i in range(n + 1)]
parties = []


def union(a, b):
    if people[a] != a:
        a = find(a)
    if people[b] != b:
        b = find(b)

    if a != b:
        people[b] = a


def find(a):
    if people[a] == a:
        return a

    root = find(people[a])
    people[a] = root
    return root


if truth[0] == 0:
    print(m)
    exit(0)

for _ in range(m):
    party = list(map(int, input().split()))
    del party[0]
    parties.append(party)

    for i in range(1, len(party)):
        union(party[0], party[i])

result = 0
for i in range(m):
    root_party = find(parties[i][0])

    has_truth = False
    for j in range(1, len(truth)):
        root_truth = find(truth[j])

        if root_truth == root_party:
            has_truth = True
            break

    if not has_truth:
        result += 1

print(result)
