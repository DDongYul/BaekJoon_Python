def per(arr,n):
    rst = []
    if n>len(arr):
        return rst
    if n == 1:
        for i in arr:
            rst.append([i])
    else:
        for i in range(len(arr)):
            for j in per(arr[0:i]+arr[i+1:],n-1):
                rst.append([arr[i]]+j)

N,M = map(int,input().split())
num = sorted(list(map(int,input().split())))
for i in per(num,M):
    for j in i:
        print(j,end=" ")
    print()

