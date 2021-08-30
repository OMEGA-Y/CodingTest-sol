import sys

N, K = map(int,sys.stdin.readline().split())
data = list(range(1,N+1))
ans = []

idx = 0
while data:
    idx = (idx+K-1)%len(data)
    ans.append(data.pop(idx))

ans = ', '.join(map(str,ans))
print(f'<{ans}>')


'''내 풀이
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
data = deque([i for i in range(1,N+1)])
ans = []

for _ in range(N):
    for _ in range(K-1):
        tmp = data.popleft()
        data.append(tmp)
    ans.append(data.popleft())

ans = ', '.join(map(str,ans))
print(f'<{ans}>')
'''