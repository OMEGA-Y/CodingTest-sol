import sys
input = sys.stdin.readline

M,N = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
res = [[0]*M for _ in range(N)]

res[0][0] = matrix[0][0]
for i in range(N):
    for j in range(M):
        if i==0 and j==0:
            continue

        if i==0:
            res[i][j] = res[i][j-1] + matrix[i][j]
        elif j==0:
            res[i][j] = res[i-1][j] + matrix[i][j]
        else:
            res[i][j] = max(res[i-1][j],res[i][j-1])+matrix[i][j]

print(res[N-1][M-1])