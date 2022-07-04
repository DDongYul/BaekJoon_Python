#백준:11726번 : 2xn 타일링
#https://www.acmicpc.net/problem/11726
#핵심 아이디어 : 규칙 찾으니 피보나치

result = [1,2]
n = int(input())

for i in range(2,n):
    result.append(result[i-2] + result[i-1])

print(result[n-1] % 10007)