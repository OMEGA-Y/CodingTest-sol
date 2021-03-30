import sys
input = sys.stdin.readline

def isRight(a,b,c):
    if a == b+c or b == a+c or c == a+b:
        return 'right'
    return 'wrong'

while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break

    a,b,c = a**2,b**2,c**2
    print(isRight(a,b,c))