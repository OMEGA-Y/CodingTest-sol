num = list(input().split())
if sorted(num) == num:
    print('ascending')
elif sorted(num,reverse=True) == num:
    print('descending')
else:
    print('mixed')