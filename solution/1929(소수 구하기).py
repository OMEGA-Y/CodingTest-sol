''' 시간 더 오래 걸리는 이전 풀이(약 3배 느림)
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
'''

M, N = map(int,input().split())

if N < 2:
    prime = []
else:
    nums = [False,False] + [True] * (N-1)
    for i in range(2, int(N**0.5)+1):
        if nums[i]: #True
            nums[i*2::i] = [False] * ((N-i)//i)
    prime = [idx for idx,val in enumerate(nums) if val and idx >= M]

for i in prime:
    print(i)