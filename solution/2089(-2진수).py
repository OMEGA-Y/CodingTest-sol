N = int(input())

if N == 0:
    print(0)
else:
    ans = ''
    while N != 1:
        if abs(N)%2==1:
            N = int((N-1)/(-2))
            ans += '1'
        else:
            N = int(N/(-2))
            ans += '0'
    ans += '1'
    print(ans[::-1])