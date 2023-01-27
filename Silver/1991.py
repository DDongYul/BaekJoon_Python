import sys
input = sys.stdin.readline

def preorder(curr):
    if curr != '.':
        print(curr, end= '')
        preorder(tree[curr][0])
        preorder(tree[curr][1])

def inorder(curr):
    if curr != '.':
        inorder(tree[curr][0])
        print(curr, end='')
        inorder(tree[curr][1])

def postorder(curr):
    if curr != '.':
        postorder(tree[curr][0])
        postorder(tree[curr][1])
        print(curr, end='')

n = int(input())
tree = {}
for i in range(n):
    a,b,c = map(str,input().split())
    tree[a] = [b,c]

preorder('A')
print()
inorder('A')
print()
postorder('A')