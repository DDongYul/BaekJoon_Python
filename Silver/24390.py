time = input()
minute,second = map(int,time.split(":"))
rst = minute*6+int(second/10)

DP = [0 for _ in range(361)]
DP[1] = 2
DP[2] = 3
DP[3] = 1
for i in range(4,361):
    DP[0] = 1
    DP[i] = DP[i-1]+1
    if i-60>=0:
        DP[i] = min(DP[i],DP[i-60]+1)
    if i-6>=0:
        DP[i] = min(DP[i],DP[i-6]+1)
    if i-3>=0:
        DP[i] = min(DP[i],DP[i-3]+1)

print(DP[rst])