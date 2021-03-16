N,K = map(int,input().split())

data = list(range(1,N+1))
ans = []

idx = 0
while data:
    idx = (idx+K-1)%len(data)
    ans.append(data.pop(idx))

ans = ', '.join(map(str,ans))
print(f'<{ans}>')