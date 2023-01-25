n = int(input())
cost = list(map(int,input().split()))

dp = [0 for _ in range(n+1)]
dp[1] = cost[0]
for i in range(2,n+1):
    mx = 0
    for j in range(int(i/2),i):
        mx = max(mx,dp[j]+dp[i-j])
    mx = max(mx,cost[i-1])
    dp[i] = mx

print(dp[n])