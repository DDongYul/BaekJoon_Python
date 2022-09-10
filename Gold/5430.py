import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(0,T):
    p = sys.stdin.readline()            #함수
    n = int(sys.stdin.readline())       #리스트 원소 개수
    # li = deque(sys.stdin.readline())    #리스트 원소들
    li = deque(map(int,sys.stdin.readline().replace(',','')[1:-2]))
    flag = 0 #뒤집힌 상태면 1
    for i in p:
        if flag == 0:
            if i == 'D' and n == 0:
                print("error")
                break
            elif i =='D' and n!=0:
                li.popleft()
                n-=1
            if i =='R':
                flag = 1

        elif flag == 1:
            if i == 'D' and n == 0:
                print("error")
                break
            elif i =='D' and n!=0:
                li.pop()
                n-=1
            if i =='R':
                flag = 0
    if flag == 0:
        print(list(li))
    else:
        result = []
        for i in range(n-1,0):
            result.append(i)
        print(list(result))