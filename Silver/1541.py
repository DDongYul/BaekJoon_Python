#백준 1541번: 잃어버린 괄호
#https://www.acmicpc.net/problem/1541
#-연산자부터 다음- 연산자 사이의 값은 전부 괄호를 붙여주 최소값 나옴!

result = 0
ex = input()
ex = ex.split('-')
if ex[0].__contains__('+'):             #처음 -가 나오기 전은 더해줘야함
    temp = map(int,ex[0].split('+'))
    result += sum(temp)
else:
    result += int(ex[0])

for i in ex[1:]:                        #-나온 이후는 괄호를 통해 전부 빼줄 수 있음!
    if i.__contains__('+'):
        temp = map(int,i.split('+'))
        result -= sum(temp)
    else:
        result-= int(i)
        
print(result)