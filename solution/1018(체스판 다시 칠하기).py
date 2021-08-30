import sys
input = sys.stdin.readline

N,M = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(N)]

minCnt = sys.maxsize
for x in range(N-7):
    for y in range(M-7):
        now = matrix[x][y]
        tmp1 = 0
        tmp2 = 0
        for i in range(8):
            for j in range(8):
                if (x+i) >= N or (y+j) >= M:
                    break
                if ((x+i)%2 == x%2 and (y+j)%2 == y%2) or ((x+i)%2 == (x+1)%2 and (y+j)%2 == (y+1)%2):
                    if matrix[x+i][y+j] != now:
                        tmp1 += 1
                    else:
                        tmp2 += 1

                else:
                    if matrix[x+i][y+j] == now:
                        tmp1 += 1
                    else:
                        tmp2 += 1

        minCnt = min(minCnt,tmp1,tmp2)

print(minCnt)