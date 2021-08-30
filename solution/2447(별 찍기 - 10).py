import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def isSame(x,y,N):
    if N==3:
        arr[x+1][y+1] = " "
        return

    for i in range(x,x+N,N//3):
        for j in range(y,y+N,N//3):

            if i == x+N//3 and j == y+N//3:
                for m in range(i,i+N//3):
                    for n in range(j,j+N//3):
                        arr[m][n] = " "
            else:
                isSame(i, j, N//3)


N = int(input().rstrip())
arr = [['*']*N for _ in range(N)]

isSame(0,0,N)
for line in arr:
    print(''.join(line))

'''
좌표 찍은 지점에 '*'이 있으면 현재 배열의 가운데 부분을 공백으로 만드는 방법
'''

'''다른 사람 풀이
def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]


def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' ' * n] * n)

    return a + b + a

k = star10(int(input().rstrip()))
print('\n'.join(k))
'''