import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    visit = [0 for _ in range(N+1)]
    num = list(map(int,input().split()))

    cnt = 0
    for i in range(1,N+1):
        if visit[i]:
            continue
        cur = i
        while not visit[cur]:
            visit[cur] = 1
            cur = num[cur-1]
        cnt += 1
    print(cnt)