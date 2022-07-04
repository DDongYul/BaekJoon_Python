#백준 1065번 : 한수
#https://www.acmicpc.net/problem/1065

#핵심 아이디어: 등차수열의 성질 이용 , 99까지는 전부 한수 , 100이후부터 탐색하여 한수면 -1을 저장

lst = []
for i in range(100,1001):
    lst.append(str(i))

for index , i in enumerate(lst):
    if int(i[1]) == (int(i[0])+int(i[2]))/2:
        lst[index] = '-1'                       #한수면 -1 저장

count = 0
N = int(input())
if(N<=99):
    print(N)
else:
    for i in range(0,N-99):
        if lst[i] == '-1':
            count+=1
    print(99+count)

