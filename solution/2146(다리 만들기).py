import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def isBorder(matrix,x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    mul = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]):
            mul *= matrix[nx][ny]
            if mul == 0:
                return True
    return False

def DFS(matrix,q,count,x,y):
    matrix[x][y] = count
    if isBorder(matrix, x, y):
        q.append([x,y])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]) and matrix[nx][ny] == 1:
            DFS(matrix,q,count,nx,ny)

def BFS(matrix,q):
    count = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    dist = sys.maxsize
    while True:
        for _ in range(len(q)):  # 같은 거리를 가진 정점을 모두 돌려보고 나서 그 중에 최솟값을 반환한다. 아래 막혔던 부분에 설명해 놓았다.
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0])):
                    if matrix[nx][ny] == 0:
                        matrix[nx][ny] = matrix[x][y]
                        q.append([nx,ny])
                        count[nx][ny] = count[x][y]+1
                    else:
                        if matrix[nx][ny] == matrix[x][y]:
                            count[nx][ny] = min(count[nx][ny],count[x][y]+1)
                            continue
                        else:
                            dist = min(dist,count[nx][ny] + count[x][y])
        if dist != sys.maxsize:
            return dist

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
q = deque()

count = 2
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            DFS(matrix,q,count,i,j)
            count += 1

print(BFS(matrix,q))

'''
dfs로 라벨링(섬 구분하기 - 좌표 읽는 데에만 O(n^2))과 동시에 섬의 가장자리 좌표를 큐에 담은 후, 
모든 섬을 시작점으로 하여 bfs 돌리는(간척사업 푸는 방법) 풀이

한 위치에서 출발하여 가장 먼저 다른 번호의 섬을 발견했을 때보다 더 작은 값은 없다.
즉, 다른 번호의 섬을 발견하면 거리를 반환하여 최솟값을 갱신하러 넘어가야 한다.
'''

''' 중간에 막혔던 부분
https://www.acmicpc.net/board/view/51987
질문 검색 게시판에 다른 분이 간척사업 진행시 간략화에 지나칠 수 있는 예외가 있어 해결방법을 남겨놓으셨는데, 덕분에 해결할 수 있었다.

0회 간척:
1 1 0 0 0 2
1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
3 0 0 0 0 0
0 0 0 0 0 0

1회 간척:
1 1 1 0 2 2
1 1 0 0 0 2
1 0 0 0 0 0
3 0 0 0 0 0
3 3 0 0 0 0
3 0 0 0 0 0

2회 간척:
1 1 1 1 2 2  -> 위의 코드는 이 부분이 진행될 때 간척을 멈추고 바로 정답을 반환하는 오류를 저지릅니다. 
즉, 정답을 3으로 출력합니다.(원래 정답은 2로 나와야 한다.)

따라서, 적어도 같은 거리를 가진 모든 정점을 검사하고 나서, 
섬끼리 맞닿은 부분의 거리의 최솟값을 구해야 합니다.
'''

''' 입력 예제
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
'''
