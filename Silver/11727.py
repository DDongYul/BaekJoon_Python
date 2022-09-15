N = int(input())
data = [0,1,3]
for i in range(3,1001):
    data.append((data[i-2]*2 + data[i-1])%10007)

print(data[N])