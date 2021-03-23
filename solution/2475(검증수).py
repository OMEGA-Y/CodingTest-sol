ans = 0
for i in map(int,input().split()):
    ans += i**2

print(ans%10)