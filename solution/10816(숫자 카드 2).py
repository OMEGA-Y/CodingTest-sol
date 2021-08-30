import sys
from collections import Counter
input = sys.stdin.readline

_, have, _ = input(), Counter(input().split()), input()
ans = ""
for i in input().split():
    if i in have:
        ans += str(have[i])+" "
    else:
        ans += "0 "
print(ans)