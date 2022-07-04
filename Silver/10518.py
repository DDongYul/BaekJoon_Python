#백준 10158번 문제 : 개미
#https://www.acmicpc.net/problem/10158
#핵심 아이디어: 직접 반복문을 돌면서 좌표를 더하면 시간이 오래 걸리기 때문에, 공식을 찾아서 좌표를 계산하였다.

import sys

line1 = sys.stdin.readline()
w = int(line1.split(" ")[0])
h = int(line1.split(" ")[1])

line2 = sys.stdin.readline()
p = int(line2.split(" ")[0])
q = int(line2.split(" ")[1])

t = int(sys.stdin.readline())
t_y = t

result_x = 0
result_y = 0

if t <= (w-p):
    result_x = p+t
else:
    t -= (w-p)
    t = t%(w+w)
    p = w
    if t<w:
        result_x = w-t
    else:
        result_x = t-w

if t_y <= (h-q):
    result_y = q+t_y
else:
    t_y -= (h-q)
    t_y = t_y%(h+h)
    q = h
    if t_y<h:
        result_y = h-t_y
    else:
        result_y = t_y-h

print(result_x,result_y)
