import sys
input = sys.stdin.readline

def binarySearch(arr,start,end,N):
    ans = 0
    while (start<=end):
        cnt = 0  # 만들 수 있는 랜선의 개수
        mid = (start+end)//2
        for x in arr:
            cnt += x//mid  # mid : 랜선의 길이
        if cnt < N:
            end = mid-1
        else:
            ans = mid
            start = mid+1

    return ans

K,N = map(int,input().split())
line = []
for _ in range(K):
    line.append(int(input().rstrip()))

line.sort()
print(binarySearch(line,1,sum(line)//N,N))

# 넓은 데이터 범위에서 특정 값을 하나 찾아야 할 때 주로 이분탐색을 사용한다.
