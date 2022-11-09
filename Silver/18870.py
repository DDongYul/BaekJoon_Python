n = int(input())
graph = list(map(int,input().split()))
graph2 = list(set(graph))
graph2.sort()

dic = {graph2[i]:i for i in range(len(graph2))}
result = [0 for _ in range(n)]
for i in range(n):
    result[i] = dic[graph[i]]

for i in result:
    print(i,end=' ')


# dic = {}
# graph_copy = graph.copy()
# graph_copy.sort()
# cnt = 1
# curr = graph_copy[0]
# dic[graph_copy[0]] = 0
# for i in range(1,n):
#     if graph_copy[i] == curr:
#         continue
#     else:
#         dic[graph_copy[i]] = cnt
#         curr = graph_copy[i]
#         cnt+=1
