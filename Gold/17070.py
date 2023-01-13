import sys
input = sys.stdin.readline

rst = 0
def DFS(x,y,flag):      #flag 0:대각선 1:가로 2:세로
    global rst
    if x == N-1 and y == N-1:
        rst+=1
    if y+1<=N-1 and not graph[x][y+1] and flag!=2:      #가로
        DFS(x,y+1,1)
    if x+1<=N-1 and y+1<=N-1 and not graph[x+1][y+1] and not graph[x][y+1] and not graph[x+1][y]:   #대각선
        DFS(x+1,y+1,0)
    if x+1<=N-1 and not graph[x+1][y] and flag != 1:    #세로
        DFS(x+1,y,2)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

DFS(0,1,1)
print(rst)
