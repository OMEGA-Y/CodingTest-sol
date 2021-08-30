import sys
input = sys.stdin.readline

data = []
for i in range(int(input())):
    age, name = input().split()
    data.append([int(age),name])

data = sorted(data, key=lambda x: x[0])
# python에서 sorted 는 stable sort에 해당함
# 내부적으로는 Hybrid sort 중 Tim sort 사용

for p in data:
    print(*p)