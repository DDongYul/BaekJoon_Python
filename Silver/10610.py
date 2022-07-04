#백준 10610 : 30
#https://www.acmicpc.net/problem/10610

#핵심 아이디어:3의배수 , 10의배수 만족하여면 0이 있어야하고 있으면 일의자리에 놓고 전체 자릿수의 합이 3의배수여야함

list = []
result = ""
N = input()
for i in N:
    list.append(int(i))

if 0 in list:
   sum = sum(list)
   if sum%3 ==0:
       list.sort()
       for i in list[::-1]:
           result+=str(i)
       print(result)
   else:
       print("-1")
else:
    print("-1")
