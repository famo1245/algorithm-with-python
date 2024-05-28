# BOJ 1991
import sys
input = sys.stdin.readline

N = int(input())
empty = '.'
root = 'A'
tree = dict()

for _ in range(N):
    parent, left_child, right_child = input().split()
    tree[parent] = {}
    node = tree[parent]
    node["left"] = left_child
    node["right"] = right_child


def preorder(node):
    print(node, end='')
    now = tree[node]

    if now['left'] != empty:
        preorder(now['left'])
    if now['right'] != empty:
        preorder(now['right'])


def inorder(node):
    now = tree[node]

    if now['left'] != empty:
        inorder(now['left'])

    print(node, end='')

    if now['right'] != empty:
        inorder(now['right'])


def postorder(node):
    now = tree[node]

    if now['left'] != empty:
        postorder(now['left'])
    if now['right'] != empty:
        postorder(now['right'])
    print(node, end='')


preorder(root)
print()
inorder(root)
print()
postorder(root)
