import sys
from collections import deque

hip = []
min_num = 2^31
def insert(x):
    global min_num
    hip.append(x)
    if x < min_num:
        min_num = x

def delete():
    global min_num
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
