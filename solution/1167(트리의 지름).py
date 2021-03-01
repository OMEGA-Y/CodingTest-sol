import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().rstrip())
edges = [defaultdict(int) for _ in range(N+1)]

for _ in range(N):
    a, *b = map(int,input().split())
    for i in range(len(b)//2):
        if b[2*i] == -1:
            break
        v, c = b[2*i:2*(i+1)]

        if edges[a][v]:
            edges[a][v] = max(edges[a][v],c)
        else:
            edges[a][v] = c

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
d[idx] = 0  # 루트노드가 정해져 있지 않아 양방향으로 입력을 받기 때문에 d[idx]값이 최댓값이 아닌데 최댓값으로 나올 수 있다.
            # d[idx] = 0 으로 시작하니까 dfs의 for 문에서 idx 노드만 이미 방문했는데도 한 번 더 방문하게 된다.
print(max(d))

# 11725 다음에 푼 문제라, 노드별로 부모를 지정하고 dfs나 bfs로 부모 노드의 dist에 간선의 val 값을 더해주는 방식으로 접근했었다.
# 계속 4%에서 틀렸습니다가 떠서 결국 원인을 모른채 접근 방법을 바꿨다.