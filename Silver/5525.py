N = int(input())
M = int(input())
S = input()

rst = 0
idx=0
l = 2*N+1
p="IOI"
for i in range(N-1):
    p += "OI"

while idx <= (M-(2*N+1)+2):
    if S[idx:idx+l] == p:
        temp = 1
        temp_idx=idx+l
        flag = True
        while flag:
            if S[temp_idx:temp_idx+2] == "OI":
                temp+=1
                temp_idx = temp_idx+2
            else:
                flag=False
                idx = temp_idx
        rst+=temp
    else:
        idx+=1

print(rst)


