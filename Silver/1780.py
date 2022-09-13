import sys
N = int(sys.stdin.readline())
data = []

for i in range(0,N):
    M = list(map(int,sys.stdin.readline().split()))
    data.append(M)

count_zero = 0
count_one = 0
count_m_one = 0

def search(x,y,n):
    global count_zero,count_one,count_m_one

    curr = data[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if curr!= data[i][j]:
                curr = 2
                break

    if curr == 2:
        n //=3
        search(x,y,n)
        search(x+n,y,n)
        search(x+2*n, y, n)
        search(x, y+n, n)
        search(x, y+2*n, n)
        search(x+n, y+n, n)
        search(x+2*n, y+n, n)
        search(x+2*n, y+2*n, n)
        search(x+n, y+2*n, n)
    elif curr == 0:
        count_zero +=1
    elif curr == 1:
        count_one +=1
    elif curr == -1:
        count_m_one +=1

search(0,0,N)
print(count_m_one)
print(count_zero)
print(count_one)