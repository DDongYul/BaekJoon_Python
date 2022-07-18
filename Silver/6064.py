import sys

T = int(sys.stdin.readline())
for i in range(0,T):
    M,N,x,y = map(int,sys.stdin.readline().split())
    flag = True
    for j in range(0,N+1):
        if (M*j + (x-y))%N == 0:
            print(M*j+x)
            flag = False
            break
    if flag:
        print(-1)