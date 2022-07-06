#백준 2606번
#https://www.acmicpc.net/problem/2606
#BFS를 통해 연결 돼있으면 방문

import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dic = {}
for _ in range(0,M):
    x,y = map(int,sys.stdin.readline().split())
    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]
    if y in dic:
        dic[y].append(x)
    else:
        dic[y] = [x]


#####BFS######
queue=[1]
visited = [False]*(N+1)
visited[1] = True
while queue:
    curr = queue.pop(0)
    if curr in dic:
        for i in dic[curr]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited[1] = False
count = 0
for i in visited:
    if i:
        count +=1
print(count)
