import sys

num = []
for line in sys.stdin:
    num.append(int(line))

print(max(num))
print(num.index(max(num))+1)