num = {}
for i in range(97,123):
    num[chr(i)] = i-96

L = int(input())
data = list(input().rstrip())

res = 0
M = 1234567891
for idx,val in enumerate(data):
    res += (31**idx)*num[val]
    res %= M

print(res)