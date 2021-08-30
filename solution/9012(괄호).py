import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    data = input().strip().replace("()","")

    while data:
        k = len(data)
        data = data.replace("()","")
        if k==len(data):
            break

    if data:
        print("NO")
    else:
        print("YES")