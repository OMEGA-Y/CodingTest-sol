from collections import Counter

word = Counter(input().upper())
m = max(word.values())

tmp = []
for val,num in word.items():
    if num == m:
        tmp.append(val)

if len(tmp) > 1:
    print('?')
else:
    print(tmp[0])