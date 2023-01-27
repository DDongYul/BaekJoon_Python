import sys
input = sys.stdin.readline
from collections import deque

#start는 루트, 루트부터 탐색 시작
def search(start):
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        for i in edge[curr]:
            if not parent[i]:
                parent[i] = curr
                queue.append(i)

n = int(input())
parent = [0 for _ in range(n+1)]
edge = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

search(1)
for i in range(2,n+1):
    print(parent[i])