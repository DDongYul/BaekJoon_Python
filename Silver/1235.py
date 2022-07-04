#백준 1235번 : 학생 번호
#https://www.acmicpc.net/problem/1235
#핵심아이디어: k자리수 만큼 문자열 자르고 리스트에 담은 뒤 중복 검사, 중복된게 없으면 k 리턴

def sol(k,string):
    length = len(string)
    return string[length-k:]            #문자열 뒤에서부터 k자리수만큼 반환하는 함수

N = int(input())
num_lst = []
for i in range(0,N):
    num = input()
    num_lst.append(num)

length = len(num_lst[0])    #문자열들의 총 자릿수
k = 1
temp_lst = []               #중복검사를 위한 리스트
flag = False
while(k<length):
    if(flag): break
    for i in num_lst:
        string = sol(k,i)
        if string not in temp_lst:          #중복되지 않으면
            temp_lst.append(string)
            if len(num_lst) == len(temp_lst):       #중복된게 없으면 while문 탈출
                flag = True
                break
        else:                              #중복되면 k값 1 증가
            k+=1
            temp_lst.clear()
            break
print(k)
