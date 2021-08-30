import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    ans = ""
    H,W,N = map(int,input().split())
    rem,div = N%H,N//H
    if not rem:
        ans += str(H)
        if div < 10:
            ans += "0"+str(div)
        else:
            ans += str(div)
    else:
        ans += str(rem)

        if div < 9:
            ans += "0" +str(div+1)
        else:
            ans += str(div+1)

    print(ans)