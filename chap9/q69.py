# BOJ 14425
# 시간 초과
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# words = []
#
# for _ in range(N):
#     words.append(input().strip())
#
# count = 0
# for _ in range(M):
#     find_word = input().strip()
#
#     if find_word in words:
#         count += 1
#
# print(count)

# 딕셔너리 이용
# 딕셔너리의 in 연산은 O(1), 리스트는 O(n)
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# words = {}
#
# for _ in range(N):
#     word = input().strip()
#     words[word] = True
#
# answer = 0
# for _ in range(M):
#     find_word = input().strip()
#     if find_word in words:
#         answer += 1
#
# print(answer)

# trie 이용
# 끝에 대한 표시가 없음
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# trie = {}
#
#
# def insert(word):
#     now = trie
#     for ch in word:
#         # trie에 문자가 없는 경우
#         if ch not in now:
#             now[ch] = {}
#         now = now[ch]
#
#
# def search(find):
#     now = trie
#     for ch in find:
#         if ch not in now:
#             return False
#         now = now[ch]
#
#     # 자식 노드가 있는 경우 일치하지 않음
#     if len(now) != 0:
#         return False
#
#     return True
#
#
# for _ in range(N):
#     word = input().strip()
#     insert(word)
#
# answer = 0
# for _ in range(M):
#     find_word = input().strip()
#     if search(find_word):
#         answer += 1
#
# print(answer)

# 반례
# 3 4
# abc
# abcd
# abcde
# abc
# abcd
# abcde
# abcdef
# output 3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trie = {}


def insert(word):
    now = trie
    for ch in word:
        # trie에 문자가 없는 경우
        if ch not in now:
            now[ch] = {}
        now = now[ch]

    # 문자열의 끝을 표시함
    now["end"] = True


def search(find):
    now = trie
    for ch in find:
        if ch not in now:
            return False
        now = now[ch]

    if "end" in now:
        return True

    # 자식 노드에 end가 없는 경우 일치하지 않음
    return False


for _ in range(N):
    word = input().strip()
    insert(word)

answer = 0
for _ in range(M):
    find_word = input().strip()
    if search(find_word):
        answer += 1

print(answer)

# trie를 클래스화
# import sys
# input = sys.stdin.readline
#
#
# # trie에서 노드에 대한 클래스
# class Node:
#     def __init__(self):
#         self.child = {}
#         self.last = False
#
#     def set_last(self):
#         self.last = True
#
#
# class Trie:
#     def __init__(self):
#         self.parent = Node()
#
#     def insert(self, string):
#         now = self.parent
#         for char in string:
#             # 문자에 해당 하는 노드가 없으면 생성
#             if char not in now.child:
#                 now.child[char] = Node()
#
#             now = now.child[char]
#
#         # 해당 노드에서 단어가 끝나는지 표시
#         now.set_last()
#
#     def search(self, find):
#         now = self.parent
#         for char in find:
#             # 문자에 해당 하는 노드가 없을때
#             if char not in now.child:
#                 return False
#
#             now = now.child[char]
#
#         # 해당 노드에서 단어가 끝나는지 확인
#         if now.last:
#             return True
#
#         return False
#
#
# N, M = map(int, input().split())
# trie = Trie()
#
# for _ in range(N):
#     word = input().strip()
#     trie.insert(word)
#
# answer = 0
# for _ in range(M):
#     find_word = input().strip()
#     if trie.search(find_word):
#         answer += 1
#
# print(answer)
