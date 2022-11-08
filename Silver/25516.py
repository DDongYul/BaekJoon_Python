import sys
from collections import deque

n,k = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(n-1):
    p,c = map(int,sys.stdin.readline().split())
    graph[p].append(c)

value = list(map(int,input().split()))

visited = [0 for _ in range(n)]
queue = deque()
queue.append([0,0])

while queue:
    curr,depth = queue.popleft()
    if depth>=k:
        continue
    else:
        visited[curr] = 1
        for node in graph[curr]:
            if not visited[node]:
                queue.append([node,depth+1])
                visited[node] = 1

result = 0
for i in range(n):
    if visited[i] == 1 and value[i] == 1:
        result +=1

print(result)



