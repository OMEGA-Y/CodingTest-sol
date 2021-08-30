N, B = map(int,input().split())

change = [i for i in range(10)]+[chr(i) for i in range(65,91)]

ans = ""
while N:
    ans += str(change[N%B])
    N = int(N/B)

print(ans[::-1])