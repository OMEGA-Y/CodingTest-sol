import sys
from collections import defaultdict
input = sys.stdin.readline

N,M,B = map(int,input().split())
num = defaultdict(int)
for _ in range(N):
    row = list(map(int,input().split()))
    for j in row:
        num[j] += 1

time = sys.maxsize
h=0
for i in range(257):
    plus, minus = 0,0
    for val,cnt in num.items():
        if val > i:
            minus += cnt*(val-i)
        elif val < i:
            plus += cnt*(i-val)

    if plus > minus+B:
        continue

    if time >= minus*2+plus:
        time = minus*2+plus
        h = i

print(f'{time} {h}')

'''이분탐색으로 풀어보려했으나 실패...
import sys
from collections import defaultdict
input = sys.stdin.readline

N,M,B = map(int,input().split())
num = defaultdict(int)
for _ in range(N):
    row = list(map(int,input().split()))
    for j in row:
        num[j] += 1

num = sorted(num.items())
cal = [0]*(num[-1][0]+1)

s,e = 0, num[-1][0]
minTime = sys.maxsize
plus,minus = 0,0

while s <= e:
    mid = (s+e)//2
    block = B
    for val,cnt in num:
        if mid > val:
            block -= cnt*(mid-val)
            plus += cnt*(mid-val)
        elif mid < val:
            block += cnt*(val-mid)
            minus += 2*cnt*(val-mid)
    if block >= 0 and plus+minus <= minTime:
        if plus+minus < minTime:
            if plus >= minus:
                e = mid -1
            else:
                s = mid+1
            h = mid
            minTime = plus+minus
        else:
            h = max(h,mid)
            s = mid+1
    else:
        e = mid-1

print(f'{minTime} {h}')
'''

'''이분탐색 풀이 반례
7 7 6000
30 21 48 55 1 1 4
0 0 0 0 0 0 0
15 4 4 4 4 4 8
20 40 60 10 20 30 2
1 1 1 1 1 1 9
24 12 33 7 14 25 3
3 3 3 3 3 3 32

Output : 1166 30
Answer : 879 10

기준 숫자를 잡았을 때 이전 시간보다 적게 걸렸다고 해서 숫자 값을 항상 올리는게 성립하지 않아서 그런 것 같다.
쌓는게 시간이 적게 걸리고 인벤토리에 블록을 추가하는게 더 오래 걸리기 때문에 이전 시간보다 적게 걸리면 기준 숫자를 올려야 효율적이라고 생각했다.
하지만 쌓아야 할 블록 수가 너무 많으면 오히려 기준 숫자를 내리는게 시간이 더 적게 걸릴 수도 있다.
이분탐색을 사용하기에 적합하지 않은 문제 같다.
'''