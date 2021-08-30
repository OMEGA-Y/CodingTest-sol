absolutes = [4,7,12]
signs = [True,False,True]
ans = 0
for pair in zip(absolutes,signs):
    if pair[1]:
        ans += pair[0]
    else:
        ans -= pair[0]

print(ans)