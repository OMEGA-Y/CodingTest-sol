import sys
from collections import deque
input = sys.stdin.readline

def BFS(edges,visit,startNode):
    q = deque([startNode])
    visit[startNode] = 1

    while q:
        cur = q.popleft()
        for e in edges[cur]:
            if not visit[e]:
                visit[e] = visit[cur]*(-1)
                q.append(e)
            else:
                if visit[e] == visit[cur]:
                    return False
    return True

K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    edges = [[] for _ in range(V+1)]
    visit = [0 for _ in range(V+1)]

    for _ in range(E):
        a,b = map(int,input().split())
        edges[a].append(b)
        edges[b].append(a)

    for i in range(1,V+1):
        if not visit[i]:
            flag = BFS(edges, visit, i)
            if not flag:
                print("NO")
                break

        if i==V:
            print("YES")

''' 이분 그래프 - https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html
이분 그래프인지 확인하는 방법
- BFS, DFS 탐색

BFS, DFS로 탐색하면서 정점을 방문할 때마다 두 가지 색 중 하나를 칠한다.
다음 정점을 방문하면서 자신과 인접한 정점은 자신과 다른 색으로 칠한다.
탐색을 진행할 때 자신과 인접한 정점의 색이 자신과 동일하면 이분 그래프가 아니다.

BFS의 경우 정점을 방문하다가 만약 같은 레벨에서 정점을 다른 색으로 칠해야 한다면 무조건 이분 그래프가 아니다.
(이분 그래프는 BFS를 할 때 같은 레벨의 정점끼리는 모조건 같은 색으로 칠해진다.)
모든 정점을 다 방문했는데 위와 같은 경우가 없다면 이분 그래프이다.

연결 성분의 개수(Connected Component)를 구하는 방법과 유사하다.
모든 정점을 방문하며 간선을 검사하기 때문에 시간 복잡도는 O(V+E)로 그래프 탐색 알고리즘과 같다.

이때 주의할 점은 연결 그래프와 비연결 그래프(고립된 노드 또는 그래프가 있는 경우)를 둘 다 고려 해야한다는 것이다.
그래프가 비연결 그래프인 경우 모든 정점에 대해서 확인하는 작업이 필요하다.
-> dfs를 모든 정점에 대해 해봐야 할까?
-> 비연결 그래프인 경우 여러 개의 그래프 중 하나라도 사이클이 존재하면 바로 False 판정을 하고 이분 그래프가 아니다라고 출력하면 된다.
'''

'''
색을 칠하면서 그래프를 순회하는데, 자식 노드들을 자신의 색과 다른 색으로 칠한다.
자식 노드가 이미 방문 당했으면 그 색이 자신의 색과 다른지 확인하다. 
다르면 계속 진행하고, 같으면 이미 이분 그래프일 수가 없으므로 종료한다.
'''