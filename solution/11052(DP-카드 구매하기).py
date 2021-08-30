import sys
input = sys.stdin.readline

N=int(input())
dp = [0]+list(map(int,input().split()))

for i in range(2,N+1):
    for j in range(1,i):
        dp[i] = max(dp[i],dp[j]*int((i/j))+dp[i%j])

print(dp[N])


# dp는 역시 점화식을 잘 세워야지