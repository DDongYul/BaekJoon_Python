import sys
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

white = 0
blue = 0
def search(x1,y1,x2,y2):
    global white
    global blue
    if x1==x2 and y1 == y2:
        if graph[x1][y1] == 0:
            white+=1
        else:
            blue+=1
        return

    flag = check(x1,y1,x2,y2)
    if flag:
        if graph[x1][y1] == 0:
            white+=1
        else:
            blue+=1
        return
    else:
        d = int((x2-x1+1)/2)-1
        search(x1,y1,x1+d,y1+d)
        search(x1+d+1,y1,x2,y1+d)
        search(x1,y1+d+1,x1+d,y2)
        search(x1+d+1,y1+d+1,x2,y2)

def check(x1,y1,x2,y2):
    curr = graph[x1][y1]
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if graph[i][j] != curr:
                return False
    return True

search(0,0,N-1,N-1)
print(white)
print(blue)