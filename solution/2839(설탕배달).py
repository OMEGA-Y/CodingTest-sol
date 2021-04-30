import sys
sys.setrecursionlimit(10**6)

N = int(input())
dp = [-1,-1,-1,1,-1,1,2,-1]+[0]*(N-7)
if N >= 8:
    for i in range(8,N+1):
        if dp[i-3] == -1:
            if dp[i-5] == -1:
                dp[i] = -1
            else:
                dp[i] = dp[i-5]+1
        elif dp[i-5] == -1:
            dp[i] = dp[i-3]+1
        else:
            dp[i] = min(dp[i-3],dp[i-5])+1
print(dp[N])