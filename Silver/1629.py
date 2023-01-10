def solution(A,B,C):
    if B == 1:
        return A%C
    if B%2 == 0:
        temp = solution(A,int(B/2),C)
        return  (temp*temp) % C
    else:
        return  (solution(A,B-1,C)*A) % C

a,b,c = map(int,input().split())
print(solution(a,b,c))

