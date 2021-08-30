import sys
from collections import deque
input = sys.stdin.readline

front = deque(list(input().rstrip()))
end = deque([])
N = int(input())

for _ in range(N):
    a, *b = input().split()
    if a=='P':
        front.append(b[0])
    elif a=='L':
        if front:
            tmp = front.pop()
            end.appendleft(tmp)
    elif a=='D':
        if end:
            tmp = end.popleft()
            front.append(tmp)
    elif a=='B':
        if front:
            front.pop()

print(''.join(front+end))

# insert와 remove 사용하면 시간초과 남
# python의 자료구조 list는 연속적인 메모리 공간에 원소를 저장하기 때문이다.

'''다른 사람 풀이(리스트의 끝에서만 pop과 append를 하고 마지막에 reverse 이용
from sys import stdin

stack1 = list(stdin.readline().strip())
stack2 = []
n = int(input())

for command in stdin:
    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            continue
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
        else:
            continue
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
        else:
            continue
    else:
        stack1.append(command[2])

print(''.join(stack1 + list(reversed(stack2))))
'''