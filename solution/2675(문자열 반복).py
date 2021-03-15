import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, S = input().split()
    ans = ""
    for i in list(S):
        ans += i*int(R)
    print(ans)