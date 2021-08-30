import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def draw(x,y):
    arr[x][y] = "*"
    arr[x+1][y-1] = "*"
    arr[x+1][y+1] = "*"
    arr[x+2][y-2:y+3] = ["*"]*5

def triangle(row,col,N):
    if N==3:
        draw(row,col)
        return

    triangle(row,col,N//2)
    triangle(row+N//2,col-N//2,N//2)
    triangle(row+N//2,col+N//2,N//2)

N = int(input().rstrip())
arr = [[' ']*(2*N) for _ in range(N)]

triangle(0,N-1,N)

for line in arr:
    print(''.join(line))


'''다른 사람 풀이
이런 생각 어떻게 하는건지 신기하다.. 꼭대층부터 바닥층까지 차례로 쌓아나가는 방식이다.
import math
List = ['*', '* *', '*****']

def printStar(List):
    max_len = len(List[-1])
    for i in range(len(List)):
        new_line = List[i] + ' '* (max_len - 2*i) + List[i]
        List.append(new_line)
    return List

n = int(input())
iter = int(math.log(n/3, 2))      # N = 3*(2^k)이니까 log로 구하면 딱 반복해야 하는 횟수만큼만 반복하게 된다.
for i in range(iter):
    List = printStar(List)
for i in range(len(List)):
    print(List[i].center(len(List[-1]), ' '))  
                # center 함수는 정의된 문자열 앞과 뒤를 특정문자(여기서는 공백)로 채운 뒤 중앙에 정렬하는 방식이다.
'''