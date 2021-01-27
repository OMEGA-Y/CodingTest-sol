import sys
from math import gcd
input = sys.stdin.readline

for _ in range(int(input())):
    sum = 0
    a, *b = map(int,input().split())
    for i in range(a-1):
        for j in range(i+1,len(b)):
            sum += gcd(b[i],b[j])
    print(sum)