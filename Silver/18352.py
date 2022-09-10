import sys
from collections import deque
dic = {}        #한 도사에서 다른 도시로 이동할 수 있는 정보를 담는 딕셔너리
data = list(map(int,sys.stdin.readline().split()))
N = data[0] #도시의 개수
M = data[1] #도로의 개수
K = data[2] #최단거리
X = data[3] #출발 도시 번호
for _ in range(0,M):
    load = tuple(map(int,sys.stdin.readline().split()))
    if load[0] in dic:
        dic[load[0]].append(load[1])
    else:
        dic[load[0]] = [load[1]]                #dic = {1:[2] , 2:[3,4]} 형태로 거리정보 저장

visit = [False] * (N+1)
visit[X] = True
depth = [0] * (N+1)
queue = deque()
queue.append(X)
result = []
curr_depth = 0
while queue:
    curr_node = queue.popleft()
    if curr_node in dic:
        for i in dic[curr_node]:
            if not visit[i]:
                queue.append(i)
                depth[i] = depth[curr_node]+1
                if depth[i] == K:
                    result.append(i)
                visit[i] = True

if result:
    result.sort()
    for data in result:
        print(data)
else:
    print(-1)

