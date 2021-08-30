import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(matrix, n, m, count, x, y):
    matrix[x][y] = 0
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if matrix[nx][ny] == 1:
                count = dfs(matrix, n, m, count+1, nx, ny)

    return count

while True:
    n,m = map(int,input().split())
    if n == 0:
        break
    matrix = [list(map(int,input().rstrip().split())) for _ in range(m)]

    cnt = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                dfs(matrix, n, m, 1, i, j)
                cnt += 1

    print(cnt)