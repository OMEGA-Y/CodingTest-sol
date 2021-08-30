import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(matrix, n, count, x, y):  # count : 집이 몇 개인지 세는 용도
    matrix[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >=0 and ny < n:
            if matrix[nx][ny] == 1:
                count = dfs(matrix, n, count+1, nx, ny)

    return count

N = int(input())
matrix = [list(map(int,input().rstrip())) for _ in range(N)]

apartment_block = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            apartment_block.append(dfs(matrix, N, 1, i, j))

print(len(apartment_block))
for num in sorted(apartment_block):
    print(num)