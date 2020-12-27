import sys
input = sys.stdin.readline

'''sol1
def LCM(A,B):
    min=A
    if A>B:
        min=B
        if A % min == 0:
            return min
    else:
        if B % min ==0:
            return min

    ans=1
    for i in range(1,min+1):
        if A%i==0 and B%i==0:
            ans=i

    return ans

for _ in range(int(input())):
    A,B = map(int, input().split())
    print(int(A*B/LCM(A,B)))
'''

# sol2
import math
for _ in range(int(input())):
    A,B = map(int, input().split())
    print(int(A*B/math.gcd(A,B)))
