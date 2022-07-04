#백준 1058번: 친구
#https://www.acmicpc.net/problem/1058
#직접 친구인 경우와 2-친구인 경우를 구분하여 생각
#직접친구는 Y일때 , 2-친구는 A,B가 C와 둘다 아는 사이 일때 이므로 C의 입장에서 둘다 친구인 경우를 담음 이떄, 중복될 수 있으니 중복검사 해줌

import sys

friend_list = []
N=int(sys.stdin.readline())
for i in range(0,N):
    friend_list.append((sys.stdin.readline().split()))

result = []
for i in range(0,N):
    for j in range(0,N):
        if friend_list[i][0][j] == 'Y':
            result.append((i,j))                #직접 친구인 경우

for i in range(0,N):
    for j in range(0,N):
        for k in range(j+1,N):
            if friend_list[i][0][j] == 'Y' and friend_list[i][0][k] == 'Y':
                if (j,k) not in result:
                    result.append((j,k))
                    result.append((k, j))       #2-친구인 경우

dic = {}
for i in result:
    if i[0] in dic:
        dic[i[0]] +=1
    else:
        dic[i[0]] = 1

if dic:
    print(max(dic.values()))
else:
    print(0)
