import sys
input = sys.stdin.readline

N = int(input().rstrip())
m = [0]*(N+1)
m[1] = 1

line = list(map(int,input().rstrip()))
for i in range(2,N+1):
    if line[i-1] == 0:
        m[i] = 0
    else:
        m[i] = m[i-1] + m[i-2]

print(m[N])
