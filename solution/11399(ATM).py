input()
num = list(map(int,input().split()))
num.sort()

res = 0
for i in range(len(num)):
    res += num[i]*(len(num)-i)

print(res)

'''다른 사람 풀이
a = int(input())
total = 0
cur = 0
l = list(map(int, input().split()))

l.sort()
for x in l:
    cur += x
    total += cur
print(total)
'''