from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
data = defaultdict(int)
for i in range(N):
    data[int(input())] += 1

large = 0
ans = 0
for key, value in data.items():
    if value > large:
        ans = key
        large = value
    elif value == large:
        if key < ans:
            ans = key

print(ans)


# 또 다른 풀이
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
data = Counter(map(int, sys.stdin))
print(max(data.items(), key=lambda x: (x[1], -x[0]))[0])
# 개수로 오름차순 정렬 후, 같을 경우 큰 숫자가 앞으로 오게 key로 정렬
# reverse 된 후 가장 첫 번째 원소를 출력함

''' python.org 문서 - max 
max(iterable, *[, key, default])

Return the largest item in an iterable or the largest of two or more arguments.

If multiple items are maximal, the function returns the first one encountered.
This is consistent with other sort-stability preserving tools such as
 sorted(iterable, key=keyfunc, reverse=True)[0] and heapq.nlargest(1, iterable, key=keyfunc).
 
요약하면 max(built in func)도 key를 지정할 수 있고, 
sorted(iterable, key=keyfunc, reverse=True)[0] 와 같은 역할을 한다.
'''