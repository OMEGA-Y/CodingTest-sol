import sys
input=sys.stdin.readline

def merge(a,b):
    global cnt
    la,lb=len(a),len(b)
    i,j=0,0
    temp=[]
    while i<la and j<lb:
        if a[i] > b[j]:
            temp.append(b[j])
            j += 1
            cnt += la-i
        else:
            temp.append(a[i])
            i += 1
    if i == la:
        temp.extend(b[j:])
    else:
        temp.extend(a[i:])
    return temp

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    l=0
    r=len(arr)-1
    mid=(l+r)//2
    return merge(mergeSort(arr[l:mid+1]),mergeSort(arr[mid+1:]))
        # 왼쪽 절반 배열부터 재귀로 계속 쪼갠다. 그 후, 왼쪽 절반 배열에서 return이 한 번 되면 왼쪽 절반 배열의 오른쪽 절반 배열에 대해 재귀를 한다.
        # 결국 처음 배열을 절반 나눴을 때의 왼쪽 절반 배열이 재귀를 거쳐 모두 정렬된 후, 오른쪽 절반 배열이 재귀를 거쳐 정렬되는 방식이다.

n=int(input())
cnt=0
arr=list(map(int,input().split()))
mergeSort(arr)
print(cnt)

'''시간초과 나는 풀이
MergeSort 알고리즘에 맞게 구현 했으나, merge() 마지막에 for문으로 새로 정렬된 배열을 원본 배열로 옮기는 과정에서 시간초과가 나는 것 같다.
통과한 코드를 보면 배열 복사 대신에 배열을 return 하는 방식으로 진행한다.

import sys
input = sys.stdin.readline

def merge(start,mid,end):
    global cnt  # 함수 안에서 전역변수(global variable)를 사용하려면 global keyword를 사용해 선언한다.
    i = start  # 왼쪽 리스트 시작 인덱스
    j = mid+1  # 오른쪽 리스트 시작 인덱스
    tmp = []  # 정렬될 새로운 리스트

    while i<=mid and j<=end:
        if num[i] <= num[j]:
            tmp.append(num[i])
            i += 1
        else:
            tmp.append(num[j])
            j += 1
            cnt += mid-i+1

    if i==mid+1:
        tmp.extend(num[j:])
    else:
        tmp.extend(num[i:mid+1])

    for i in range(start,end+1):
        num[i] = tmp[i-start]


def mergeSort(start,end):
    if start<end:
        mid = (start+end)//2
        mergeSort(start,mid)
        mergeSort(mid+1,end)
        merge(start,mid,end)

N = int(input().rstrip())
num = list(map(int,input().split()))

cnt = 0
mergeSort(0,N-1)
print(cnt)
'''