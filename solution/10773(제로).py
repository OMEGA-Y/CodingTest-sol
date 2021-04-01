import sys

K = int(input())
stack = []
for line in sys.stdin:
    num = int(line.rstrip())
    if num==0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))