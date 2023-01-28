import itertools
N,M = map(int,input().split())
num = [i for i in range(1,N+1)]
rst = list(itertools.combinations(num,M))
for i in rst:
    for j in i:
        print(j,end=" ")
    print()