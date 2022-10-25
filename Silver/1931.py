import sys
N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
data.sort(key=lambda x : (x[1],x[0]))
curr = data[0]

end = data[0][1]
count = 1
for i in range(1,N):
    if data[i][0]>=end:
        count+=1
        end = data[i][1]

print(count)