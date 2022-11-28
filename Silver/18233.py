import sys
import itertools
input = sys.stdin.readline

N,P,E = map(int,input().split())
member = []
for _ in range(N):
    member.append(tuple(map(int,input().split())))
temp = [i for i in range(N)]
sol = list(itertools.combinations(temp,P))
flag = True
for i in sol:
    min_m = 0
    max_m = 0
    for j in i:
        min_m += member[j][0]
        max_m += member[j][1]
    if min_m<=E<=max_m:
        temp = i
        flag = False
        break
if flag:
    print(-1)
else:
    res = [0 for _ in range(N)]
    for i in temp:
        res[i] = member[i][0]
    for i in temp:
        while res[i]<=member[i][1]:
            if sum(res)==E:
                print(" ".join(list(map(str,res))))
                exit()
            elif res[i] == member[i][1]:
                break
            else:
                res[i]+=1






