import sys,heapq
from collections import defaultdict
input = sys.stdin.readline

def prim(edges, N):
    queue = []
    heapq.heappush(queue, [0, 0, 1])

    visit = [False for _ in range(N*2)]
    sum =0
    while queue:
        h = heapq.heappop(queue)
        if visit[h[2]]:
            continue
        else:
            visit[h[2]] = True
            sum += h[0]

        for e in edges[h[2]]:
            if visit[e[0]]: continue
            heapq.heappush(queue, [e[1], h[2], e[0]])

    return sum

N = int(input())
node = defaultdict(int)
edges = [[] for _ in range(N*2)]

vertices = set()
idx = 1
for _ in range(N):
    u, v, c = input().split()
    if u not in vertices:
        vertices.add(u)
        node[u] = idx
        idx += 1
    if v not in vertices:
        vertices.add(v)
        node[v] = idx
        idx += 1

    num_u = node[u]
    num_v = node[v]

    flag = True
    for i in edges[num_v]:
        if i == [num_u, int(c)]:
            flag = False
            break

    if flag:
        edges[num_u].append([num_v,int(c)])
        edges[num_v].append([num_u,int(c)])

print(prim(edges, N))