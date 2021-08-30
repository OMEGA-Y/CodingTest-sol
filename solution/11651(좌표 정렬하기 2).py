import sys
input = sys.stdin.readline

coordinate = []

for _ in range(int(input())):
    coordinate.append(list(map(int,input().split())))

coordinate = sorted(coordinate, key=lambda x: (x[1],x[0])) # x : 좌표를 의미(coordinate의 원소)
                                                           # y좌표 기준 오름차순 정렬, 같을 경우 x좌표 기준 오름차순 정렬
for c in coordinate:
    print(*c)