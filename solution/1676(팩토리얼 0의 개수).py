num = 1
for i in range(1,int(input())):
    num *= i+1

cnt = 0
num = str(num)[::-1]
for i in num:
    if not int(i):
        cnt += 1
    else:
        break

print(cnt)