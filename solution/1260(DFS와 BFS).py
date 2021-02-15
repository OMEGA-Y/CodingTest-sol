from collections import deque
import sys
input = sys.stdin.readline

def dfs(edges, startNode):
    visit = []
    q = deque([startNode])

    while q:
        cur = q.pop()
        if cur not in visit:
            visit.append(cur)
            q.extend(edges[cur])
    return visit

def bfs(edges, startNode):
    visit = []
    q = deque([startNode])

    while q:
        cur = q.popleft()
        if cur not in visit:
            visit.append(cur)
            q.extend(reversed(edges[cur]))
    return visit

N,M,V = map(int,input().split())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int,input().split())
    if v1 in edges[v1]:
        continue
    edges[v1].append(v2)
    edges[v2].append(v1)

for e in edges:
    e.sort(reverse=True)

print(*dfs(edges,V))
print(*bfs(edges,V))

'''
다른사람풀이
import sys

n ,m ,v = map(int, sys.stdin.readline().strip().split())

edge = [[] for _ in range(n+1)]

for i in range(m):
	a, b = map(int, sys.stdin.readline().strip().split())
	edge[a].append(b)
	edge[b].append(a)
	
for e in edge:
	e.sort(reverse=True)
	
def DFS():
	dfs = []
	stack = [v]
	visit = [0 for i in range(n+1)]
	while stack:
		node = stack.pop()
		if visit[node]:
			pass
		else:
			visit[node] = 1
			dfs.append(node)
			stack += edge[node]
	return dfs
	
def BFS():
	bfs = []
	que = [v]
	visit = [0 for i in range(n+1)]
	visit[v] = 1
	while que:
		node = que.pop()
		bfs.append(node)
		for i in reversed(edge[node]):
			if visit[i]:
				continue
			visit[i] = 1
			que = [i] + que    => list는 스택구조로 작용해서 pop을 하면 맨 뒤의 원소부터 빠짐
			                      그래서 queue는 먼저 들어온대로 나가야 하니까 나중에 나가야 할걸 맨 앞에 추가
	return bfs

print(" ".join(map(str, DFS())))
print(" ".join(map(str, BFS())))

'''