import sys
input = sys.stdin.readline

def check(x):
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        elif i == '{':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return "NO"
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return "NO"
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return "NO"
    return "YES"

T = int(input().rstrip())
for _ in range(T):
    x = input().rstrip()
    print(check(x))