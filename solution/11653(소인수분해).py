N = int(input())

num = N
for i in range(2,N+1):
    while not num%i:
        print(i)
        num = int(num/i)


'''처음 풀이 - 시간이 너무 오래 걸림
nums = [False,False] + [True] * (N-1)
for i in range(2, int(N**0.5)+1):
    if nums[i]: #True
        nums[i*2::i] = [False] * ((N-i)//i)
prime = [idx for idx,val in enumerate(nums) if val]


for p in prime:
    while N%p==0:
        print(p)
        N = int(N/p)
    if N==0:
        break
'''