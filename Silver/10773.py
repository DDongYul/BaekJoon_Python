#백준 10773번 : 제로
#https://www.acmicpc.net/search#q=10773&c=Problems
#핵심 아이디어: 반복문으로 input을 받을 때는 sys.stdin.readline()을 사용하면 시간이 훨씬 단축된다!!

import sys

num_list = []
index = 0
K = int(sys.stdin.readline())

for i in range(0,K):
    num = int(sys.stdin.readline())
    if num!=0:
        num_list.append(num)
        index+=1
    elif num == 0 and index>=0:
        num_list.pop()
        index-=1
print(sum(num_list))

