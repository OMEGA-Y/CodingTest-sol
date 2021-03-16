import sys
input = sys.stdin.readline

N,M = map(int,input().split())
num = []
for i in map(int,input().split()):
    if i < M:
        num.append(i)

res = -sys.maxsize
for i in range(len(num)-2):
    for j in range(i+1,len(num)-1):
        for k in range(j+1,len(num)):
            if num[i]+num[j]+num[k] > M:
                continue
            res = max(num[i]+num[j]+num[k],res)

print(res)