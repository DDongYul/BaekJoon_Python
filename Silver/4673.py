#백준 4673번 : 셀프 넘버
#https://www.acmicpc.net/problem/4673

#핵심 아이디어: 1부터 10000까지 저장된 리스트를 선언한 뒤 1부터 탐색하여 self넘버가 아니면 -1로 바꿔줌
def initnum(num):       #숫자 + 각 자리 수 더한값 리턴해주는 함수
    temp = 0
    string = str(num)
    for i in string:
        temp += int(i)
    result = int(string) + temp
    return result

lst = []
for i in range(0,10001):
    lst.append(str(i))          #index를 편리하기 위해 0부터 리스트를 만듬

for i in range(1,10001):
    if lst[i] != '-1':
        num = int(lst[i])
        while num<=10000:
            num = initnum(num)
            if num <=10000:
                lst[num] = '-1'     #1부터 탐색하여 생성할 수 있는 수(self넘버가 아닌 수)를 -1로 변환

for i in range(1,10001):
    if lst[i] != '-1':
        print(lst[i])