import sys
from collections import deque
input = sys.stdin.readline

def DFS(edges, visit, startNode):
    q = deque([startNode])
    while q:
        cur = q.pop()
        if not visit[cur]:
            visit[cur] = 1
            q += edges[cur]

N,M = map(int,input().split())
edges = [[] for _ in range(N+1)]
visit = [0 for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

cnt = 0
for i in range(1,N+1):
    if not visit[i]:
        DFS(edges, visit, i)
        cnt += 1

print(cnt)