import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))

P.sort()
count = 0
result = 0
for i in P:
    count+=i
    result+=count

print(result)