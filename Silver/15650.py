def comb(arr,n):
    rst = []
    if n > len(arr):
        return rst
    elif n == 1:
        for i in arr:
            rst.append([i])
    else:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:],n-1):
                rst.append([arr[i]]+j)
    return rst

N,M = map(int,input().split())
num = [i for i in range(1,N+1)]
result = comb(num,M)
for i in result:
    for j in i:
        print(j,end=' ')
    print()

