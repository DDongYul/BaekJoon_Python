import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def search(pre_start,pre_end,in_start,in_end):
    if (pre_start>pre_end) or (in_start>in_end):
        return
    root = pre[pre_start]
    root_index = node_index[root]
    left_count = root_index-in_start
    right_count = in_end-root_index

    search(pre_start+1,pre_start+left_count,in_start,in_start+left_count-1)
    search(pre_end-right_count+1,pre_end,in_end-right_count+1,in_end)
    print(root)

T = int(input())
for _ in range(T):
    n = int(input())
    pre = list(map(int,input().split()))
    ino = list(map(int, input().split()))
    node_index = [0 for _ in range(n+1)]
    for i in range(0,n):
        node_index[ino[i]]=i
    search(0,n-1,0,n-1)


