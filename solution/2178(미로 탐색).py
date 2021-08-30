import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def findRoute(maze):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    q = deque([(0,0)])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        if x == (len(maze)-1) and y == (len(maze[0])-1):
            return maze[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0])) and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                maze[nx][ny] = maze[x][y]+1
                q.append((nx, ny))
                visited[nx][ny] = 1

N, M = map(int,input().split())
maze = [list(map(int,input().rstrip())) for _ in range(N)]

print(findRoute(maze))

'''
DFS는 기본적으로 최단 거리를 구하는데 적절하지 못한 탐색 방법이다.
모든 가능한 경로를 탐색하는데 특정 지점에 처음으로 방문했을 때까지의 거리가 최단 경로라는 보장이 없기 때문이다.
지수 시간복잡도가 된다.
따라서 이 문제는 BFS로 풀어야 한다.
BFS로 방문하면 N*M 행렬에서는 방문하는 지점까지의 최단 거리를 보장해주는 것 같다.

참고로, recursion limit의 기본값은 1000이다.
문제의 크기에 따라 다르지만 여기서 N과 M이 100까지 가능하므로 100*100 = 10000까지 될 수 있다.
따라서 recursion limit을 더 크게 set 해야 한다.
'''