import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    lst = [input() for _ in range(n)]
    lst.sort(key=len)
    flag = False
    for i in range(n):
        for j in range(i+1,n):
            print(lst[j][0:len(lst[i]) - 1].rstrip())
            if lst[j][0:len(lst[i])-1]:
                flag = True
    if flag:
        print("No")
    else:
        print("Yes")

