import sys
input = sys.stdin.readline

N = int(input())
start_h = []
start_m = []
end_h = []
end_m = []
for i in range(N):
    line = list(input().rstrip().split(':'))
    mid = line[1].split(' ~ ')
    start_h.append(line[0])
    start_m.append(mid[0])
    end_h.append(mid[1])
    end_m.append(line[2])

a,b,c,d = start_h[0],start_m[0],end_h[0],end_m[0]
for i in range(1,N):
    if a < start_h[i]:
        a = start_h[i]
        b = start_m[i]
    elif a == start_h[i]:
        b = max(start_m[i],b)

    if c > end_h[i]:
        c = end_h[i]
        d = end_m[i]
    elif c == end_h[i]:
        d = min(end_m[i],d)

if a > c:
    print(-1)
elif a == c:
    if b > d:
        print(-1)
else:
    print(f'{a}:{b} ~ {c}:{d}')