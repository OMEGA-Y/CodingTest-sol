N = int(input())
num = list(map(int,input().split()))
m = max(num)
for i in range(N):
    num[i] = num[i]/m*100

print(sum(num)/N)