#백준 1916번 최소비용 구하기
#https://www.acmicpc.net/problem/1916
#우선순위 큐 , 다익스트라
import sys
from heapq import heappush,heappop

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edge = [[]for _ in range(N+1)]
for _ in range(0,M):
    a,b,c = map(int,sys.stdin.readline().split())
    edge[a].append((b,c))

s,e = map(int,sys.stdin.readline().split())

cost = [100000001]*(N+1)
cost[s] = 0
heap = []
heappush(heap,[0,s])

while heap:
    w,n = heappop(heap)
    if w>cost[n]:
        continue
    for nn,ww in edge[n]:
        new_cost = w + ww
        if new_cost<cost[nn]:
            cost[nn] = new_cost
            heappush(heap,[new_cost,nn])
print(cost[e])



