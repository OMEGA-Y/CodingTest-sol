import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

if N==0 or M==0:
    print(0)
else:
    T = N//2
    if T > M:
        T = M

    rem = M+N-3*T
    if K <= rem:
        print(T)
    else:
        K -= rem
        T -= K//3
        if K%3:
            T -= 1
        print(T)