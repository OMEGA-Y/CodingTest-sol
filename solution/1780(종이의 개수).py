import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def isSame(x,y,N):
    init = arr[x][y]
    if N==1:
        num[init] += 1
        return

    for i in range(x,x+N):
        for j in range(y,y+N):
            if arr[i][j] != init:
                N = N // 3
                for i in range(3):
                    for j in range(3):
                        isSame(x + N * i, y + N * j, N)
                return

    num[init] += 1

N = int(input().rstrip())
arr = [list(map(int,input().split())) for _ in range(N)]
num = [0,0,0]

isSame(0,0,N)
print(f'{num[-1]}\n{num[0]}\n{num[1]}')
# num[-1] = num[2]와 같다.