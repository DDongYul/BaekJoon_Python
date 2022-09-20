import sys
from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

visited = [ [0 for i in range(N)] for i in range(N) ]

def DFS(n):
    queue = deque()
    queue.append(n)
    while queue:
        curr = queue.popleft()
        for index,data in enumerate(graph[curr]):
            if data == 1 and visited[n][index] == 0:
                visited[n][index] = 1
                queue.append(index)

for i in range(0,N):
    DFS(i)

for i in visited:
    li = list(map(str,i))
    print(" ".join(li))

