#백준 1652번 누울 자리를 찾아라 문제
#https://www.acmicpc.net/problem/1652

n = int(input())
list = []
for i in range(0,n):
    str = input()
    list.append(str)

column_count = 0        #열의 개수
line_count = 0          #행의 개수
j=0
for i in range(0,n):
    while(j<n-1):       #j의 index가 n-1보다 작을떄 까지 반복
        if list[i][j] =='.' and list[i][j+1] =='.':
            column_count+=1
            while list[i][j] != 'X' and j<n-1:          #연속인 경우 다음 짐(X)이 나올때 까지 j증가
                j+=1
        else:
            j+=1
    j=0

for i in range(0,n):
    while(j<n-1):
        if list[j][i] =='.' and list[j+1][i] =='.':
            line_count+=1
            while list[j][i] != 'X' and j<n-1:
                j+=1
        else:
            j+=1
    j=0

print(column_count,line_count)
