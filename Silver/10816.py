#백준 10816번 : 숫자카드 2
#https://www.acmicpc.net/problem/10816
#핵심아이디어: 카드들의 개수 정보를 담은 딕셔너리를 만들고 , 주어진 정수카드와 비교하여 딕셔너리에 있으면 개수를 출력하고 없으면 0 출력

import sys

N = int(sys.stdin.readline())
num_list = sys.stdin.readline().split()
M = int(sys.stdin.readline())
user_list = sys.stdin.readline().split()

for i in range(0,N):
    num_list[i] = int(num_list[i])

result = {}
user_list2 = []
for i in range(0,M):
    user_list[i] = int(user_list[i])
    user_list2.append(user_list[i])

num_list.sort()
user_list.sort()

index_n = 0
index_m = 0

while index_n<N and index_m<M:
    if user_list[index_m] == num_list[index_n]:
        if num_list[index_n] not in result:
            result[num_list[index_n]] = 1
        else:
            result[num_list[index_n]] +=1
        index_n+=1
    elif user_list[index_m] > num_list[index_n]:
        index_n+=1
    elif user_list[index_m] < num_list[index_n]:
        index_m+=1

for i in user_list2:
    if i in result:
        print(result[i], end=' ')
    else: print(0 , end=' ')


#
# import sys
#
# N = int(input())
# arr1 = list(map(int, sys.stdin.readline().split()))
# M = int(input())
# arr2 = list(map(int, sys.stdin.readline().split()))
# dic = dict()
# for key in arr1:
#     if key not in dic:
#         dic[key] = 1
#     else:
#         dic[key] += 1
#
# result = list()
# for i, key in enumerate(arr2):
#     if key in dic:
#         result.append(dic[key])
#     else:
#         result.append(0)
# answer = ""
# for i in result:
#     answer += str(i) + " "
# print(answer.rstrip())

