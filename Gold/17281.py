import sys
from itertools import *

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    li.append(data)

def simulation(inning,order):
    # print(order)
    player = 0
    score = 0
    curr_inning = 1
    out_count = 0
    base = []
    while curr_inning<=inning:
        curr_player = order[player] - 1    #현재 타자
        # print("curr_player" , curr_player)
        heat = li[curr_inning-1][curr_player]  #타자의 타격 결과
        # print("heat",heat)
        # print(heat)
        if heat == 0:
            out_count +=1
        elif heat == 1:
            base.append(1)
        elif heat == 2:
            base.append(1)
            base.append(0)
        elif heat == 3:
            base.append(1)
            for _ in range(2):
                base.append(0)
        elif heat == 4:
            base.append(1)
            for _ in range(3):
                base.append(0)

        if out_count == 3:
            for i in base[:-3]:
                if i ==1:
                    score+=1
            curr_inning+=1
            out_count = 0
            base = []
        player = (player+1)%9
    return score

#2~9까지 랜덤 리스트 만들고 1을 index3에 삽입 하면 될듯
dataset = [2,3,4,5,6,7,8,9]
printlist = list(permutations(dataset,8))
order_list = []
for i in printlist:
    temp = list(i)
    temp.insert(3,1)
    order_list.append(temp)
result = []
for i in order_list:
    result.append(simulation(N,i))
print(max(result))