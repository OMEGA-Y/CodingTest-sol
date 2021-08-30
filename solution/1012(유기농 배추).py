import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def cal(matrix,x,y):
    matrix[x][y] = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >=0 and nx < N and ny >=0 and ny < M and matrix[nx][ny] == 1:
            cal(matrix,nx,ny)

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        Y,X = map(int,input().split())
        matrix[X][Y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                cal(matrix,i,j)
                cnt += 1

    print(cnt)