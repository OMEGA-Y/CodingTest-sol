import sys
from collections import Counter
input = sys.stdin.readline

def binarySearch(arr,start,end,M):
    ans = 0
    while (start<=end):
        cnt = 0
        mid = (start+end)//2
        for key,val in arr.items():
            if key < mid:
                continue
            cnt += (key-mid)*val
        if cnt < M:
            end = mid-1
        else:
            ans = mid
            start = mid+1

    return ans

N,M = map(int,input().split())
tree = Counter(map(int,input().split()))

print(binarySearch(tree,0,max(tree.keys())-1,M))

# 같은 높이의 tree가 있을 경우, 한 번에 절단기와의 차이를 더해주면 시간 절약이 되므로 Counter를 사용함.
# 처음에 Counter 사용 안 했는데, 사용하니까 시간이 6배 빨라지고 메모리도 더 적게 사용함.