import sys

N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

result = [0]*N
result[0] = num[0]
for i , n in enumerate(num[1:]):
    result[i+1] = max(result[i] + n , n)

print(max(result))