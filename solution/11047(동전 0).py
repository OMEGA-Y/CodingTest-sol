import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coins = [0]*N
for i in range(N):
    coins[i] = int(input())

cnt = 0
for coin in sorted(coins,reverse=True):
    while K >= coin:
        cnt += K//coin
        K %= coin
    if K == 0:
        print(cnt)
        break