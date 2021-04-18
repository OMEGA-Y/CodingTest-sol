import sys
input = sys.stdin.readline

N = int(input())
p = []
for _ in range(N):
    p.append(list(map(int,input().split())))

num = [1]*N
for i,val in enumerate(p):
    for k in range(i+1,N):
        if val[0]<p[k][0] and val[1]<p[k][1]:
            num[i] += 1
        elif val[0]>p[k][0] and val[1]>p[k][1]:
            num[k] += 1

print(*num)