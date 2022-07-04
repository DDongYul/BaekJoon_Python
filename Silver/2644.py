#백준 2644 촌수계산
#https://www.acmicpc.net/problem/2644
#사용 알고리즘: BFS
#BFS를 통해 촌수를 구해줌

import sys
n = int(sys.stdin.readline())
x1,y1 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
dic = {}
for _ in range(0,m):
   x,y = map(int,sys.stdin.readline().split())
   if x not in dic:
       dic[x] = [y]
   else:
       dic[x].append(y)
   if y not in dic:
       dic[y] = [x]
   else:
       dic[y].append(x)                 #양방향 그래프를 위해 x,y | y,x둘다 넣어줌

queue = [x1]
depth = [0]*(n+1)
visited = [False]*(n+1)
visited[x1] = True
while queue:
    curr = queue.pop(0)                 #선입선출 해줘야한다!
    visited[curr] = True
    for i in dic[curr]:
        if not visited[i]:
            queue.append(i)
            depth[i] = depth[curr] + 1
            visited[i] = True

if depth[y1] == 0:
    print(-1)
else:
    print(depth[y1])
