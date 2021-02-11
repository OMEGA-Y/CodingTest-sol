M, N = map(int,input().split())

prime = set([i for i in range(3,N+1,2)])
for i in range(3,N+1,2):
    if i in prime:
        prime -= set([i for i in range(i*2,N+1,i)])

prime = [2]+list(prime)
prime.sort()

for i in prime:
    if i < M:
        pass
    else:
        print(i)