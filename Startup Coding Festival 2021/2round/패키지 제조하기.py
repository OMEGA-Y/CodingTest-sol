import sys
from math import log2
from collections import deque
input = sys.stdin.readline

def dfs(tree,exp_parent,root,depth):
    q = deque()
    q.append(root)
    depth[root]=0

    while q:
        p = q.popleft()
        for i in tree[p]:
            if depth[i]==-1:
                q.append(i)
                exp_parent[i][0] = p
                depth[i] = depth[p]+1

def compute_exp_parent(exp_parent,N,logN):
    for j in range(1, logN):
        for i in range(1, N + 1):
            exp_parent[i][j] = exp_parent[exp_parent[i][j-1]][j-1]

def find(x,y,depth,exp_parent,logN):
    if depth[x] >= depth[y]:
        return 0

    for i in range(logN-1,-1,-1) :
        if depth[y]-depth[x] >= (1 << i):
            y = exp_parent[y][i]

    if x==y:
        return 1

N,Q = map(int,input().split())
tree = [[] for _ in range(N + 1)]

logN = int(log2(N) + 1)
depth = [-1 for _ in range(N + 1)]
exp_parent = [[0 for _ in range(logN)] for _ in range(N + 1)]

values = [0]*(N+1)
for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    values[v]=1

root = 0
for k in range(1,N+1):
    if not values[k]:
        root = k
        break

dfs(tree, exp_parent, root, depth)
compute_exp_parent(exp_parent,N,logN)

for _ in range(Q):
    a,b = map(int,input().split())
    if find(a,b,depth,exp_parent,logN):
        print('yes')
    else:
        print('no')