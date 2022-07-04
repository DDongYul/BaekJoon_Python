#백준 2961번 : 도영이가 만든 맛있는 음식
#https://www.acmicpc.net/problem/2961
#사용 알고리즘 : 브루트포스 , 비트맵
#각 재료마다 비트와 매핑하여 1이면 재료를 사용, 0이면 사용하지 않는 식으로 하여 모두 검사

import sys
N = int(sys.stdin.readline())
data = []
for _ in range(0,N):
    a,b = map(int,sys.stdin.readline().split())
    data.append((a,b))

mask = 1023         #1<=N<=10
result = []
for i in range(1,pow(2,N)):
    taste1 = 1
    taste2 = 0
    bit = i&mask            #1~2^N까지 검사
    bit = bin(bit)[2:]      #bin 사용하면 0b1000 식으로 출력, 0b 없애줌
    for j in range(0,len(bit)):
        if bit[j] == '1':
            taste1*=data[len(bit)-j-1][0]
            taste2+=data[len(bit)-j-1][1]
    result.append(abs(taste2-taste1))

print(min(result))
