#1927번 : 최소힙
#https://www.acmicpc.net/problem/1927

import sys
from collections import deque
hip = []
class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

root = Node(2^31) #root
def insert(num):
    node = Node(num)
    curr = root
    flag = True
    while flag:
        if node.data < curr.data
    global root
    hip.append(x)
    if x < min_num:
        min_num = x

def delete():
    global root
    if hip:
        print(hip.pop(hip.index(min_num)))
        if hip:
            min_num = min(hip)
        else:
            min_num = 0
    else:
        print(0)

N = int(sys.stdin.readline())
for _ in range(0,N):
    x = int(sys.stdin.readline())
    if x == 0:
        delete()
    else:
        insert(x)
