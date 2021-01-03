import sys
input = sys.stdin.readline

stack = 0
cnt = 0

data = input().strip().replace('()','0')
for i in data:
    if i == '(':
        stack += 1
    elif i == '0':
        cnt += stack
    else:
        stack -= 1
        cnt += 1

print(cnt)

'''구현 원리 기본
여는 괄호를 만나면 전부 스택에 push,
닫는 괄호를 만나면 스택에 pop하고,
  괄호가 레이저면 스택 사이즈 만큼 count,
  괄호가 파이프 끝이면 +1 만큼 count

스택 사이즈 = 레이저로 절단될 쇠막대기의 개수를 의미
'''