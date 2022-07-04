import sys

N,M = map(int , sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

left = min(tree)
right = max(tree)
pivot = int((left+right) / 2)
length = 0
result_length = 9
while (right-left)>1:
    for data in tree:
        if data - pivot>0:
            length += (data-pivot)
            result_length = length
    if M<length:
        left = pivot
        pivot = int((left + right)/2)
        length = 0
    elif M>length:
        right = pivot
        pivot = int((left + right) / 2)
        length = 0
    else:
        break
print(pivot)