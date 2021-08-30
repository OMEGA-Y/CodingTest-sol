a,b = input().split()
if a[2] > b[2]:
    print(a[::-1])
elif a[2] == b[2]:
    if a[1] > b[1] or (a[1]==b[1] and a[0]>b[0]):
        print(a[::-1])
    else:
        print(b[::-1])
else:
    print(b[::-1])
