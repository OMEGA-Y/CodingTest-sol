import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input().rstrip())
edges = [defaultdict(int) for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int,input().split())
    if edges[a][b]: # 중복 간선 담기지 않도록 방지
        edges[a][b] = max(edges[a][b],c)
        edges[b][a] = max(edges[b][a],c)
    else:
        edges[a][b] = c
        edges[b][a] = c

def dfs(edges,dist,startNode=1):
    for key,val in edges[startNode].items():
        if not dist[key]:
            dist[key] = dist[startNode]+val
            dfs(edges,dist,key)


d = [0 for _ in range(N + 1)]
dfs(edges,d)
d[1] = 0

idx = 0
max_dist = 0
for i,val in enumerate(d):
    if val > max_dist:
        max_dist = val
        idx = i

d = [0 for _ in range(N + 1)]
dfs(edges,d,idx)
d[idx] = 0
print(max(d))