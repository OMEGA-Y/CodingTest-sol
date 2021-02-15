def countNum(N,num):
    cnt = 0
    while N != 0:
        cnt += N // num
        N = N // num

    return cnt

n, r = map(int,input().split())
five = 0
two = 0

if n==r or r==0:
    print(0)
else:
    print(min(countNum(n,5)-countNum(r,5)-countNum(n-r,5),countNum(n,2)-countNum(r,2)-countNum(n-r,2)))


'''또 다른 풀이
n, r = map(int,input().split())
five = 0
two = 0

if n==r or r==0:
    print(0)
else:
    for i in range(1,31):
        five += n//(5**i)-r//(5**i)-(n-r)//(5**i)
        two += n//(2**i)-r//(2**i)-(n-r)//(2**i)
    print(min(five,two))
'''