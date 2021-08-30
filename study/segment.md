# Segment tree (세그먼트 트리) - Python 코드

수를 바꾸는 과정과 수를 더하는 과정을 O(logN)에 해결 가능하다는 장점이 있다. <br>
N개의 수가 주어지고 dq = [3,5,4,...,8]에 담겨있다고 가정해보자.

Segment tree는 노드에 구간 합을 저장해놓는 트리이고, 트리는 list로 구현한다. leaf 노드에는 입력받은 N개의 수가 위치한다. 따라서 list의 크기는 N의 가장 가까운 제곱수가 되어야 하므로 list의 크기는 아래의 공식을 이용하거나 4*N으로 지정한다.

```python
from math import log2
logN = int(log2(N)+1)

tree = [0 for _ in range(2**logN)]
```

### Segment tree 초기화
```python
def init(start,end,node):
    if start==end:
        tree[node]=dq[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(start,mid,node*2)+init(mid+1,end,node*2+1)
    return tree[node]
```

### Segemnt tree 업데이트
```python
def update(start,end,node,index,diff):
    if index<start or index>end:  //index가 start와 end 사이에 있는 노드만 업그레이드 필요
        return 0

    tree[node] += diff    // 노드의 구간 합 업그레이드
    if start != end:    // leaf 노드가 아닐 경우 자식 노드도 마저 구간 합 업그레이드 필요
        mid = (start+end)//2
        update(start,mid,node*2,index,diff)
        update(mid+1,end,node*2+1,index,diff)
```
 **index** : 값을 바꾸려는 노드 번호 <br>
 **diff** : 수정할 값 <br>
 dq의 index번째 수가 a(=dq[index])에서 b로 변경될 때 diff = b-dq[index] 를 의미

### Segment tree 합
```python
def sum(start,end,node,left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree[node]

    mid = (start+end)//2
    return sum(start,mid,node*2,left,right) + sum(mid+1,end,node*2+1,left,right)
```

**left,right** : 구간 합을 하려는 범위 <br>

1. [left, right]와 [start, end]가 겹치지 않는 경우
= 구간 합을 구하려는 범위와 상관이 없는 경우
`if(left > end || right < start)`로 표현 할 수 있다.

2. [left, right]가 [start, end]를 완전히 포함하는 경우
= 구간 합 구간에 포함되는 경우
`if(left <= start && end <= right)`로 표현할 수 있다.

3. [start, end]가 [left, right]를 완전히 포함하는 경우
= 구하려는 구간 합 범위보다는 크지만 내부에 구하고자 하는 구간 합을 포함하는 경우
`return sum(tree, node*2, start, mid, left, right) + sum(tree, node*2+1, mid+1, end, left, right)`로 표현할 수 있다.

4. [left, right]와 [start, end]가 겹쳐져 있는 경우(1,2,3을 제외한 나머지 경우)
= 즉, left <= start <= right <= end 같은 경우
`return sum(tree, node*2, start, mid, left, right) + sum(tree, node*2+1, mid+1, end, left, right)`로 표현할 수 있다.

결과적으로 3,4 case는 재탐색을 해야한다.
