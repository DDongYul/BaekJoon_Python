import sys
input = sys.stdin.readline
n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = int(input())
for i in range(1,n):
    temp = list(map(int,input().split()))
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + temp[j]

print(max(max(dp)))