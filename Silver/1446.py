# N,D = map(int,input().split())
# graph = [[] for _ in range(10005)]
# distance = [i for i in range(10005)]
#
# for _ in range(N):
#     s,d,l = map(int,input().split())
#     graph[s].append([d,l])
#
# for index,i in enumerate(graph):
#     if i:
#         for j in i:
#             distance[j[0]] = min(distance[j[0]],distance[index]+j[1])
#             for k in range(j[0]+1,D+1):
#                 distance[k] = min(distance[k],distance[j[0]]+k-j[0])
# print(distance[D])

from heapq import heappush,heappop

N,D = map(int,input().split())
graph = [[] for _ in range(10005)]
cost = [100000 for i in range(10005)]

for _ in range(N):
    s,d,l = map(int,input().split())
    graph[s].append((d,l))

for i in range(D):
    graph[i].append((i+1,1))        #각 정점이 다음 정점과 1의 거리로 이어져 있다고 생각해야한다!

heap = []
heappush(heap,(0,0))

while heap:
    w,n = heappop(heap)
    if w>cost[n]:
        continue
    for nn,ww in graph[n]:
        new_cost = w + ww
        if new_cost<cost[nn]:
            cost[nn] = new_cost
            heappush(heap,[new_cost,nn])

print(cost[D])

