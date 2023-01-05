#도로는 방향 없이 양쪽에 먼저 넣음
#웜홀을 방향 있게 위에 덮어씀
#플로이드 와샬

import sys
input = sys.stdin.readline
INF = int(1e9)

TC = int(input())
for _ in range(TC):
    N,M,W = map(int,input().split())
    graph = [[INF for _ in range(N)]for _ in range(N)]
    for _ in range(M):
        S,E,T = map(int,input().split())
        graph[S-1][E-1] = min(graph[S-1][E-1],T)
        graph[E-1][S-1] = min(graph[E-1][S-1],T)
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S-1][E-1] = min(graph[S-1][E-1],-T)

    flag = False
    for i in range(N):
        if flag: break
        for j in range(N):
            if flag: break
            for k in range(N):
                graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])
                if j == k and graph[j][k]<0:
                    flag = True
                    break

    if flag:
        print("YES")
    else:
        print("NO")