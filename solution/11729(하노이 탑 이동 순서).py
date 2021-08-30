import sys
input = sys.stdin.readline

N = int(input())
cnt = [0 for _ in range(N+1)]
ord = [[] for _ in range(N+1)]
if N==1:
    print(1)
    print('1 3')
elif N==2:
    print(3)
    print(f'1 2\n1 3\n2 3')
else:
    cnt[1] = 1
    cnt[2] = 3
    ord[2] = [(1,2),(1,3),(2,3)]
    for i in range(3,N+1):
        cnt[i] = 2*cnt[i-1]+1
        for a,b in ord[i-1]:
            if a != 1:
                if a == 2:
                    a=3
                else:
                    a=2
            if b != 1:
                if b == 2:
                    b=3
                else:
                    b=2
            ord[i].append((a,b))
        ord[i].append((1,3))
        for a,b in ord[i-1]:
            if a != 3:
                if a == 1:
                    a=2
                else:
                    a=1
            if b != 3:
                if b == 1:
                    b=2
                else:
                    b=1
            ord[i].append((a,b))
    print(cnt[N])
    for num in ord[N]:
        print(*num)

'''다른 사람 풀이.. 대박!
이동 횟수와 이동 과정을 출력해야 하는데 규칙이 존재한다.
n개의 원반을 옮길 때 최소 이동 횟수는 2**n-1이다.
이동 과정은 '바로 직전 이동과정(1)' + '1 3' + '바로 직전 이동과정(2)'이 된다.
바로 직전 이동과정 (1)에서는 1은 그대로 유지되고 2와 3이 서로 바뀌어야 한다.
바로 직전 이동과정 (2)에서는 3은 그대로 유지되고 1과 2가 서로 바뀌어야 한다.
난 그래서 최소 이동횟수를 f(n) = 2*f(n-1)+1로 생각했었다. 

n = int(input())
str = "1 3\n"
for i in range(n-1):
    str_f = str.replace("3","4").replace("2","3").replace("4","2")
    str_m = "1 3\n"
    str_b = str.replace("1","4").replace("2","1").replace("4","2")
    str = str_f+str_m+str_b
print(2**n-1)
print(str)
'''