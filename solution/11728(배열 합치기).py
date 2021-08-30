''' 통과한 풀이
input()
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(*sorted(A+B))
'''

# 아래 풀이는 틀렸습니다로 나오는데 원인을 모르겠음 => 해결함
# 반례 예시 : -1 들어가는 경우, 배열의 원소가 각각 하나인 경우, 배열의 원소가 하나는 여러 개 하나는 한 개인 경우
# 반례(숫자가 입력으로 들어오는 경우 : 음수, 공백 주의) 해결했더니 통과
# 위의 풀이보다 시간이 약 2배나 더 걸리네...

import sys
input = sys.stdin.readline

input()
A = input().split()
B = input().split()

res = ""
while True:
    if not A:
        res += ' '.join(reversed(B))
        break
    elif not B:
        res += ' '.join(reversed(A))
        break
    else:
        if int(A[-1]) > int(B[-1]):
            res += A[-1]+" "
            A.pop()
        elif int(A[-1]) == int(B[-1]):
            res += A[-1]+" "+A[-1]+" "
            A.pop()
            B.pop()
        else:
            res += B[-1]+" "
            B.pop()

print(*reversed(res.rstrip().split(" ")))
