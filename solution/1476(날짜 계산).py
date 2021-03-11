import sys
input = sys.stdin.readline

E,S,M = map(int,input().split())

i,j,k = 0,0,0
while True:
    x1 = 15*i+E
    x2 = 28*j+S
    x3 = 19*k+M

    if x1 == x2 == x3:
        print(x1)
        break
    else:
        if x1<x2 or x1<x3:
            i += 1
        elif x2<x1 or x2<x3:
            j += 1
        elif x3<x1 or x3<x2:
            k += 1