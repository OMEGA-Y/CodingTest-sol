import sys
from collections import Counter
input = sys.stdin.readline

l = Counter(input().split())
print(sum(l.values()))


''' 다른 사람 풀이 - 어차피 중복 단어도 모두 카운트하니까 공백 개수 +1 하면 그 문장의 전체 단어 개수가 됨..
s = input().strip()
print(s.count(' ') + 1 if s else 0)
'''

''' 또 다른 사람 풀이
import sys
s = sys.stdin.read().strip()
if not s:
    print("0")
else:
    print(len(s.split(" ")))
'''