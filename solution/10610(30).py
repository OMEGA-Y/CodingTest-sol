import sys
input = sys.stdin.readline

N = list(map(int,input().rstrip()))
N.sort(reverse=True)

if sum(N)%3==0 and N[-1] == 0:
    print(''.join(map(str,N)))
else:
    print(-1)