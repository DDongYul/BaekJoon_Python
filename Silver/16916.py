S = input()
P = input()

j = 0
i = 0
flag = 0
temp = 0
while i < len(S):
    print(i , j)
    if S[i] == P[j]:
        if j==0:
            temp = i
        j+=1
        if j == len(P):
            flag = 1
            break
    else:
        j = 0
        i = temp
    i+=1
print(flag)