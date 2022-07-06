#백준 7576번 토마토:
#https://www.acmicpc.net/problem/7576
#BFS(2차원)
#Queue로 쓰이는 경우(선입선출) deque가 list보다 훨씬 빠름 / 이 문제 deque안쓰면 시간초과!
import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())
status = []
for _ in range(0,N):
    data = list(map(int,sys.stdin.readline().split()))
    status.append(data)

##상하좌우로 갈 수 있는지 체크하는 함수들
def left(x):
    if x[1] ==0:
        return False
    elif status[x[0]][x[1]-1] == -1:
        return False
    return True

def right(x):
    if x[1] ==M-1:
        return False
    elif status[x[0]][x[1]+1] == -1:
        return False
    return True

def up(x):
    if x[0] == 0:
        return False
    elif status[x[0]-1][x[1]] == -1:
        return False
    return True

def down(x):
    if x[0] == N-1:
        return False
    elif status[x[0]+1][x[1]] == -1:
        return False
    return True

queue = deque()
depth = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for i in range(0,N):
    for j in range(0,M):
        if status[i][j] == 1:
            queue.append((i,j))
            visited[i][j] = True
        if status[i][j] == -1:
            depth[i][j] = -1

while queue:
    curr = queue.popleft()
    if left(curr):
        if not visited[curr[0]][curr[1]-1]:
            queue.append((curr[0],curr[1]-1))
            depth[curr[0]][curr[1]-1] = depth[curr[0]][curr[1]] + 1
            visited[curr[0]][curr[1]-1] = True
    if right(curr):
        if not visited[curr[0]] [curr[1] + 1]:
            queue.append((curr[0], curr[1]+1))
            depth[curr[0]][curr[1] + 1] = depth[curr[0]][curr[1]] + 1
            visited[curr[0]][curr[1]+1] = True
    if up(curr):
        if not visited[curr[0]-1][curr[1]]:
            queue.append((curr[0]-1, curr[1]))
            depth[curr[0]-1][curr[1]] = depth[curr[0]][curr[1]] + 1
            visited[curr[0]-1][curr[1]] = True
    if down(curr):
        if not visited[curr[0]+1][curr[1]]:
            queue.append((curr[0] +1, curr[1]))
            depth[curr[0]+1][curr[1]] = depth[curr[0]][curr[1]] + 1
            visited[curr[0]+1][curr[1]] = True

flag = False
day = 0
for i in range(0,N):
    for j in range(0,M):
        if depth[i][j] != -1 and visited[i][j] == False:
            flag = True
        if depth[i][j] > day:
            day = depth[i][j]
if flag:
    print(-1)
else:
    print(day)
