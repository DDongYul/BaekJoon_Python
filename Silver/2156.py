import sys
input = sys.stdin.readline

n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))

if n == 1:
    print(grape[0])
elif n == 2:
    print(grape[0]+grape[1])
else:
    dp = [[0 for _ in range(2)] for _ in range(n)]      #[0]: 현재 잔이 2번째 잔인 경우 [1]: 현재 잔이 첫번째 잔인 경우
    dp[0][0] = grape[0]
    dp[0][1] = grape[0]
    dp[1][0] = grape[0] + grape[1]
    dp[1][1] = grape[1]

    for i in range(2,n):
        mx = 0
        for j in range(i-3,i-1):
            mx = max(mx,dp[j][0],dp[j][1])
        dp[i][1] = mx+grape[i]
        dp[i][0] = dp[i - 1][1] + grape[i]

    rst = 0
    for i in dp:
        rst = max(rst,max(i))
    print(rst)

