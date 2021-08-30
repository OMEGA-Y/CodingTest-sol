import sys
input = sys.stdin.readline

a = [0 for i in range(26)]
for i in input().strip():
    a[ord(i)-ord('a')] += 1

print(*a)

'''방법2 - count() 함수 사용
data = input()
for i in range(26):
    print(data.count(chr(97+i)),end=' ')
    
# str.count() 함수 : str에 매개변수로 주어진 아이템이 몇 번 count 됐는지 횟수를 반환
'''

'''방법3 - zip, Counter 사용
from collections import Counter
import string

init = dict(zip(string.ascii_lowercase, [0 for _ in range(26)]))
data = sorted(Counter(input().rstrip()).items(), key=lambda x:x[0])
for chr,cnt in data:
    init[chr] = cnt

print(*init.values())
'''