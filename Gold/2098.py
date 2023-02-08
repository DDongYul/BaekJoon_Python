import sys
input = sys.stdin.readline
INF =  987654321

def search(curr_cost,visited,curr):
    # print("curr_cost",curr_cost)
    # print("visited",visited)
    # print("curr",curr)
    global rst
    if all(visited):
        rst = min(rst,curr_cost+edge[curr][0])
        return
    visited_node_list = []
    not_visited_node_list = []
    for i in range(n):
        if visited[i]:
            visited_node_list.append(i)
        else:
            not_visited_node_list.append(i)

        min_w = INF
    for i in range(n):
        for j in not_visited_node_list:
            if i == j:
                continue
            min_w = min(min_w,edge[i][j])
    # print("min_w",min_w)
    if (curr_cost+(min_w*len(not_visited_node_list)))>rst:
        return
    else:
        for i in not_visited_node_list:
            cost = INF
            for j in visited_node_list:
                if edge[j][i]<cost:
                    cost = edge[j][i]
                    curr_index = i
            if cost!=INF:
                visited[i] = 1
                # print("cost",cost)
                search(curr_cost+cost,visited,curr_index)
                visited[i] = 0


n = int(input())
edge = []
for _ in range(n):
    edge.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if i!=j and edge[i][j]==0:
            edge[i][j] = INF
