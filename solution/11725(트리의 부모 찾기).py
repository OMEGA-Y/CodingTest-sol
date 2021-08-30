import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

parent = [0 for _ in range(N+1)]
parent[1] = 1

q = deque([1])
while q:
    cur = q.popleft()

    for i in edges[cur]:
        if not parent[i]:
            parent[i] = cur
            q.append(i)

for i in parent[2:N+1]:
    print(i)