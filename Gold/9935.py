str1 = list(input())
str2 = list(input())
str_map = [0 for _ in range(len(str1))]
end_str = str2[-1]

stack1 = []
for index,i in enumerate(str1):
    if i==end_str:
        stack1.append((i,index))
        if len(stack1)>=len(str2):
            flag = True
            k = 0
            for j in range(len(stack1)-len(str2),len(stack1)):
                if stack1[j][0] != str2[k]:
                    flag=False
                k+=1
            if flag:
                for j in range(len(str2)):
                    a,b = stack1.pop()
                    str_map[b] = 1
            else:
                stack1.clear()
        else:
            stack1.clear()
    else:
        stack1.append((i,index))

if all(str_map):
    print("FRULA")
else:
    rst = []
    for i in range(len(str1)):
        if str_map[i] == 0:
            rst.append(str1[i])
    print("".join(rst))
