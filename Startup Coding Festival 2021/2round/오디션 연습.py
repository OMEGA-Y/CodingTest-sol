import sys
input = sys.stdin.readline

N,T = input().rstrip().split()
T = list(map(int,T.split(':')))
T = T[0]*3600+T[1]*60+T[2]

time = []
for _ in range(int(N)):
    t = list(map(int,input().rstrip().split(':')))
    t = t[0]*60+t[1]
    time.append(t)

res = [0]*len(time)
for idx,val in enumerate(time):
    cnt = 1
    tmp = val
    for i in range(idx+1,len(time)):
        if tmp >= T:
            res[idx] = cnt
            break
        else:
            tmp += time[i]
            cnt += 1

m = -sys.maxsize
p = 0
for idx,val in enumerate(res):
    if m < val:
        m = val
        p = idx+1
print(f'{m} {p}')