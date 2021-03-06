import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def isSame(x,y,N):
    init = arr[x][y]
    if N==1:
        ans.append(init)
        return

    for i in range(x,x+N):
        for j in range(y,y+N):
            if arr[i][j] != init:
                N = N // 2
                ans.append('(')
                for i in range(2):
                    for j in range(2):
                        isSame(x + N * i, y + N * j, N)
                ans.append(')')

                return

    ans.append(init)

N = int(input().rstrip())
arr = [list(input()) for _ in range(N)]

ans = []
isSame(0,0,N)
print(''.join(ans))