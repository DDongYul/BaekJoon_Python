n,a,b = map(int,input().split())
lst = [i for i in range(n+2)]
if a>b: a,b = b,a
lst[a+1]=1
lst[b+1]=1
for i in range(a+1,n+1):
    if i<=b:
        lst[i] = min(lst[i],lst[i-a-1]+1)
    else:
        lst[i] = min(lst[i],lst[i-a-1]+1,lst[i-b-1]+1)

print(lst[n])