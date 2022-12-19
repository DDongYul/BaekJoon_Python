import sys
input = sys.stdin.readline

def sol(n):
    s = int(n)
    if s == 0:
        return "INSOMNIA"
    lis = set([0,1,2,3,4,5,6,7,8,9])
    temp = set([])
    while len(temp) != 10:
        l = list(n)
        for i in l:
            temp.add(i)
        n = str(int(n)+s)
    return str(int(n)-s)

T = int(input())
for i in range(T):
    curr = input().strip()
    rst = sol(curr)
    print("Case #{0}: {1}".format(i+1,rst))
