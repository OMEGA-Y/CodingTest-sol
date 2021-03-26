import sys
from collections import deque

N = int(input())
num = deque([int(i) for i in sys.stdin])

stack = [1]
res = '+\n'
for i in range(2,N+2):
    while stack:
        if stack[-1] == num[0]:
            stack.pop()
            num.popleft()
            res += '-\n'
        else:
            break

    if i==N+1:
        continue

    stack.append(i)
    res += '+\n'

if stack:
    print('NO')
else:
    print(res)