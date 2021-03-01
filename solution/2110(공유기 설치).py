import sys
input = sys.stdin.readline

def binarySearch(arr,start,end,C):
    ans = 0
    while (start<=end):
        cnt = 1
        pos = arr[0]
        mid = (start+end)//2

        for val in arr:
            if val >= pos+mid:
                pos = val
                cnt += 1
            if cnt == C:
                break
        if cnt != C:
            end = mid-1
        else:
            ans = mid
            start = mid+1
    return ans

N,C = map(int,input().split())
arr = [int(input().rstrip()) for _ in range(N)]
arr.sort()

print(binarySearch(arr,0,(arr[-1]-arr[0])//(C-1),C))