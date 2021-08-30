N,K = map(int,input().split())

ans = 1
K = min(K,N-K)

i = 0
for _ in range(K):
    ans *= (N-i)
    i += 1

for i in range(2,K+1):
    ans //= i

print(ans)