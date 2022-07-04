#백준 9461변 : 파도반 수열
#https://www.acmicpc.net/problem/9461
#p[n] = p[n-1] + p[n-5]

import sys

def solution(N):
    p = [0,1,1,1,2]
    if(N<=4):
        return p[N]
    else:
        for i in range(5,N+1):
            p.append(p[i-1] + p[i-5])
    return p[N]

T = int(sys.stdin.readline())
for i in range(0,T):
    N = int(sys.stdin.readline())
    print(solution(N))