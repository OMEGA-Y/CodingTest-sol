# 2차원 배열을 만들어서 접근. MLE 해결
# 배열의 a-1에서 b-1까지 기존 값에 k씩 더해준 후, 마지막에 배열의 max 값을 출력하는 문제이다.
# 시작점 a-1에만 k를 더해주고 끝나는 지점 b에는 -k를 더해준다.
# 마지막에 인덱스 0부터 차례대로 값을 더해가며 배열을 돌면서,
# b-1까지만 k를 더해줘야 하므로 b에서 -k와 상쇠되어 0을 더해주는 효과를 준다.
# 이런 생각 어떻게 하는 건지 대단하다.

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
queries = [list(map(int,input().split())) for _ in range(M)]

arr = [0 for _ in range(N)]
for i in range(len(queries)):
    low = queries[i][0]
    high = queries[i][1]
    value = queries[i][2]
    arr[low-1] += value

    if high < len(arr):
        arr[high] -= value

max = 0
cur = 0
for i in range(len(arr)):
    cur = cur+arr[i]
    if max < cur:
        max = cur

print(max)



''' if 아래 문법이 새로운 리스트를 생성하는 것이므로 메모리 점유가 늘어나게 된다. MLE발생하는 풀이(제한 256M)
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

printer = [0 for _ in range(N)]
for _ in range(M):
    a,b,k = map(int,input().split())
    if a>N:
        continue
    elif a<1 and b>N:
        printer = [printer[i] + k for i in range(N)]
    elif a<1:
        printer[:b] = [printer[i] + k for i in range(b)]
    elif b>N:
        printer[a-1:] = [printer[i] + k for i in range(a-1,N)]
    else:
        printer[a-1:b] = [printer[i]+k for i in range(a-1,b)]

print(max(printer))
'''

'''
[입력]
5 3 # 축길이 프린팅수
1 2 100 # a 에서 b까지 k만큼 프린트
2 5 100
3 4 100

[출력]
200
'''