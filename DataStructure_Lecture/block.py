import sys
from collections import deque
input = sys.stdin.readline

T = len(input().split())
top = [0]*T

s = sys.maxsize
for i in range(T):
    top[i] = deque(list(map(int,input().split())))
    s = min(s,sum(top[i]))

while True:
    change = s
    for i in range(T):
        while sum(top[i]) > s:
            top[i].popleft()
            s = min(s,sum(top[i]))
    if s == change:
        break
print(s)