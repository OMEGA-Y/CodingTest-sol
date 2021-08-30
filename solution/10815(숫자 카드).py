# set 사용하면 주석 처리해놓은 코드보다 3배 더 빠름
import sys
input = sys.stdin.readline

_, have, _ = input(), set(input().split()), input()
ans = ""
for i in input().split():
    if i in have:
        ans += "1 "
    else:
        ans += "0 "
print(ans)

''' TLE 는 안 났지만 시간이 좀 많이 걸림
import sys
input = sys.stdin.readline

input()

have = list(map(int,input().split()))
have_card = [0 for i in range(min(have),max(have)+1)]
for i in have:
    have_card[i] = 1

input()
query = list(map(int,input().split()))
for i in query:
    if have_card[i]:
        print(1,end=" ")
    else:
        print(0,end=" ")
'''