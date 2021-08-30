import sys
input = sys.stdin.readline

def cal(matrix,x,y,num):
    if x+num > N or y+num > N:
        return False

    cnt = 0
    for i in range(num):
        cnt += sum(matrix[x+i][y:y+num])

    if cnt == num*num:
        return True
    else:
        return False

N = int(input())
size = [0]*(N+1)
matrix = []
for _ in range(N):
    row = list(map(int,input().rstrip()))
    size[1] += sum(row)
    matrix.append(row)

for num in range(2,N+1):
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==1:
                if cal(matrix,i,j,num):
                    size[num] += 1

print(f'total: {sum(size)}')
for i in range(1,N+1):
    if size[i]==0:
        break
    print(f'size[{i}]: {size[i]}')