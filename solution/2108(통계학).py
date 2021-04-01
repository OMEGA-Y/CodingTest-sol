import sys
input = sys.stdin.readline

N = int(input())
num = [0]*8001
m,n = -sys.maxsize,sys.maxsize
s=0
for i in range(N):
    number = int(input())
    num[number+4000] += 1
    m = max(number,m)
    n = min(number,n)
    s += number

print(round(s/N))

cnt = 0
rep = True
f = max(num)
frequency = []
for i in range(8001):
    if rep:
        cnt += num[i]
        if cnt >= N // 2 + 1:
            print(i - 4000)
            rep=False

    if num[i] == f:
        frequency.append(i-4000)

if len(frequency) >= 2:
    print(frequency[1])
else:
    print(frequency[0])
print(m-n)