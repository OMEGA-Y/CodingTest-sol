import sys
A,B,C = map(int,sys.stdin.readline().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

'''다른사람 풀이
A,B,C = map(int,input().split())
print((A+B)%C,(A%C + B%C)%C,(A*B)%C,(A%C * B%C)%C, sep="\n")
'''