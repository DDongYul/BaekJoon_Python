#백준 16198번 : 에너지 모으기
#https://www.acmicpc.net/problem/16198
#브루트포스 알고리즘 (재귀사용)

import sys
N = int(input())
l = list(map(int,sys.stdin.readline().split()))
result = []
def sol(curr,li):
    if len(li) >2:
        for i in range(1,len(li)-1):
            w = li[i-1] * li[i+1]
            temp =li.copy()
            temp.pop(i)
            sol(curr+w,temp)
    else:
        result.append(curr)

sol(0,l)
print(max(result))