

def getDistance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

interval = 1000000
Ax,Ay,Bx,By,Cx,Cy,Dx,Dy = map(int,input().split())
aDX = (Bx - Ax) / interval
aDY = (By - Ay) / interval
cDX = (Dx - Cx) / interval
cDY = (Dy - Cy) / interval

lo = 0
hi = interval

while hi-lo >= 3:
    p = (2 * lo + hi) // 3  # 내분점 구하는 공식 사용, p와 q는 항상 0 이상 interval 이하에 있다.
    q = (lo + 2 * hi) // 3

    pVal = getDistance(Ax + aDX*p, Ay + aDY*p, Cx + cDX*p, Cy + cDY*p)  # p만큼 간 거리
    qVal = getDistance(Ax + aDX*q, Ay + aDY*q, Cx + cDX*q, Cy + cDY*q)  # q만큼 간 거리

    if pVal < qVal:
        hi = q-1
    else:
        lo = p+1

min_dist = getDistance(Ax + aDX*hi, Ay + aDY*hi, Cx + cDX*hi, Cy + cDY*hi)

for i in range(lo,hi):
    tmp =  getDistance(Ax + aDX*i, Ay + aDY*i, Cx + cDX*i, Cy + cDY*i)
    min_dist = min(tmp,min_dist)

print(min_dist)

''' 삼분탐색을 사용하지 않은 풀이
import sys
input = sys.stdin.readline

def getDistance(Ax1,Ay1,Cx1,Cy1):
    return ((Ax1-Cx1)**2 + (Ay1-Cy1)**2)**0.5

interval = 1000000
Ax1,Ay1,Ax2,Ay2,Cx1,Cy1,Cx2,Cy2 = map(int,input().split())
aDX = (Ax2 - Ax1) / interval
aDY = (Ay2 - Ay1) / interval
cDX = (Cx2 - Cx1) / interval
cDY = (Cy2 - Cy1) / interval

min_dist = getDistance(Ax1,Ay1,Cx1,Cy1)
for i in range(1,interval+1):
    tmp = getDistance(Ax1+aDX*i, Ay1+aDY*i, Cx1+cDX*i, Cy1+cDY*i)
    min_dist = min(tmp,min_dist)

print(min_dist)
'''