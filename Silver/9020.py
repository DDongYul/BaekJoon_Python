#백준 9020번 : 골드바흐의 추측
#https://www.acmicpc.net/problem/9020
#소수 리스트를 선언한뒤 in으로 비교하면서 진행하면 시간초과 , 소수인지 아닌지 판별하는 함수를 하나 정의(prime)
import sys
import math

def prime(n):
    if n ==2:
        return True
    n2 = int(math.sqrt(n))+1        #소수 찾을떄 루트만큼만 찾아도 됨
    for i in range(2,n2+1):
        if n%i ==0:
            return False
    return True

def solution(n):
    if (n/2)%2 == 1:            #2로 나눈게 홀수일떄
        left = int(n/2)
        right = int(n/2)
        if prime(left):
            return (left,right)
        else:
            while not(prime(left) and prime(right)):
                left -=2
                right +=2
    else:                       #2로 나눈게 짝수일떄 (4는 2,2가 가능하므로 예외)
        if n ==4:
            return(2,2)
        left = int(n/2)-1
        right = int(n/2)+1
        if prime(left) and prime(right):
            return (left,right)
        else:
            while not(prime(left) and prime(right)):
                left -=2
                right +=2
    return (left,right)

T = int(sys.stdin.readline())
for i in range(0,T):
    N = int(sys.stdin.readline())
    sol = solution(N)
    print(sol[0] , sol[1])

