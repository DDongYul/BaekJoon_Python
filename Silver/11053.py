#DP 뒤에서부타!!
import sys
input = sys.stdin.readline

n = int(input())
per = list(map(int,input().split()))
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if per[i] > per[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))