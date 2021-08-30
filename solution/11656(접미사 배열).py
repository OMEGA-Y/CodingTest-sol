import sys
input = sys.stdin.readline().rstrip()

data = []
for i in range(len(input)):
    data.append(input[i:])

data.sort()
for i in data:
    print(i)