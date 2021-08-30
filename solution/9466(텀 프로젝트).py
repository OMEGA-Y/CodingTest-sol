import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0]+list(map(int,input().split()))
    num = [0 for _ in range(n+1)]
    q = []
    for i in graph:
        num[i] += 1

    for i in range(1,n+1):
        if num[i]==0:
            heapq.heappush(q,i)

    cnt = 0
    while q:
        n = heapq.heappop(q)

        cnt += 1
        num[graph[n]] -= 1
        if num[graph[n]] == 0:
            heapq.heappush(q,graph[n])

    print(cnt)

'''Topological Sort 사용
topological sort의 queue 버전을 응용하여 사이클에 포함되는 않는 정점 찾기
주의 : test case가 있는 문제에서는 항상 사용하는 변수들의 적절한 초기화가 중요

팀에 속하려면 = cycle이 형성되어야 한다
cycle이 형성되려면 = 다른 노드에게 pointing 되어야 한다. 즉, 지목받아야 한다.

위상 정렬에서 num[i]==0인 노드는 지목받지 못한 노드가 된다.
지목받지 못한 노드 = 어느 팀에도 속하지 않는 학생

원래는 cycle을 하나씩 찾아서 cycle에 속하지 않는 번호들을 세려고 했는데
위상 정렬로 cycle에 속하지 않는 번호를 찾는게 더 효율적인 것 같다.
'''