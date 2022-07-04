#백준 5567번: 결혼식
#https://www.acmicpc.net/problem/5567
#사용 알고리즘: BFS
#BFS를 한뒤 depth가 1또는2인것만 찾아서 출력


import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dic = {}
for _ in range(0,m):
    a,b = map(int,sys.stdin.readline().split())
    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)
    if b not in dic:
        dic[b] = [a]
    else:
        dic[b].append(a)

queue = deque()
queue.append(1)
depth =[0]*(n+1)
visited = [False]*(n+1)
visited[1] = True

while queue:
    curr = queue.popleft()              #선입선출
    if curr in dic:
        for i in dic[curr]:
            if not visited[i]:
                queue.append(i)
                depth[i] = depth[curr] + 1
                visited[i] = True

count = 0
for i in depth:
    if 1<=i<=2:
        count+=1
print(count)