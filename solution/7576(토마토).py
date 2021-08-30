import sys
from collections import deque
input = sys.stdin.readline

def bfs(matrix,m,n,ripe):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    day = -1
    while ripe:
        day += 1

        for _ in range(len(ripe)): # 초기 ripe의 길이만큼만 for문을 돌고 day를 +1 해 줌
            x,y = ripe.popleft()  # pop()을 하면 날짜를 셀 수가 없음

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >=0 and ny < m and matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    ripe.append([nx,ny])

    for val in matrix:
        if 0 in val:
            return -1
    return day

m, n = map(int,input().split())
matrix = []
ripe = deque()

for i in range(n):
    row = list(map(int,input().rstrip().split()))
    for j in range(m):
        if row[j] == 1:
            ripe.append([i,j])
    matrix.append(row)

print(bfs(matrix,m,n,ripe))

'''
하루가 지날 때마다 익은 토마토 상하좌우에 있는 토마토들이 익는다.
한 방향으로 익는 것이 아니라 익은 토마토 주변부가 익기 시작하는 것이므로 BFS로만 풀어야 한다.

처음에 익은 토마토의 위치를 파악해 queue에 넣는다.
하나씩 pop 해서 주변에 있는 토마토를 익게 하고, queue가 비워지면 하루가 지났다고 생각한다.
이전 값에 1을 더해 이전 토마토보다 하루 더 늦게 익었음을 체크한다.
마지막으로, 0이 하나라도 존재하면 밭 전체가 익지 않기 때문에 -1을 반환한다.
'''