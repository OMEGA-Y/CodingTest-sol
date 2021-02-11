A,B = map(int,input().split())
change = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input()
num = list(map(int,input().split()))
if num[0] != 0:
    change_num = ""
    for i in num:
        change_num += change[i]

    ten_num = int(change_num,A)

    rem = []
    while ten_num:
        rem.append(ten_num%B)
        ten_num = int(ten_num/B)

    rem.reverse()
    print(*rem)
else:
    print(0)