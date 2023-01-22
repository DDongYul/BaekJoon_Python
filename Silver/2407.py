def pascal(n,r):
    rst = 0
    for i in range(1,n):
        rst+= com[i][r-1]
    return rst

n,m = map(int,input().rstrip().split())
com = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    com[i][0] = 1
    com[i][1] = i
    com[i][i] = 1

for i in range(3,n+1):
    for j in range(2,i):
        com[i][j] = pascal(i,j)


print(com[n][m])
