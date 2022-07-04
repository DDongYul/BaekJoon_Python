#백준 7795번: 먹을 것인가 먹힐 것인가
#https://www.acmicpc.net/problem/7795
#두개의 포인터 사용 , 정렬한 뒤 A가 B보다 크면 B의 인덱스 증가시키고 작거나 같으면 A의 인덱스 증가시키면서 count 늘려줌
import sys

T=int(sys.stdin.readline())
for i in range(0,T):
    line2 = list(map(int,sys.stdin.readline().split()))
    N = line2[0]
    M=line2[1]
    listA = list(map(int,sys.stdin.readline().split()))
    listB = list(map(int,sys.stdin.readline().split()))

    listA.sort()
    listB.sort()

    indexA=0
    indexB=0
    count = 0

    while indexA < N:
        if listA[indexA] <= listB[indexB]:
            count += indexB
            indexA+=1

        elif listA[indexA] > listB[indexB]:
            while listA[indexA] > listB[indexB]:
                if indexB == M-1:
                    count += indexB+1
                    indexA+=1
                    break
                indexB+=1
    print(count)

