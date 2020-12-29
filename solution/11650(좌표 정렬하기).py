import sys
input = sys.stdin.readline

coordinate = []

for _ in range(int(input())):
    coordinate.append(list(map(int,input().split())))

coordinate = sorted(coordinate, key=lambda x: (x[0],x[1])) # x : 좌표를 의미(coordinate의 원소)
for c in coordinate:
    print(*c)