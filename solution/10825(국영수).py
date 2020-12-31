import sys
input = sys.stdin.readline

N = int(input())
data = [None]*N
for i in range(N):
    data[i] = list(input().split())

data = sorted(data,key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for student in data:
    print(student[0])