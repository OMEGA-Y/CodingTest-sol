import sys

def check(x):
    stack = []
    cnt = 0
    flag = False
    for i in x:
        if flag and not i=='"':
            continue

        if i=='"' and cnt==0:
            cnt = 1
            flag = True
        elif i=='"' and cnt==1:
            cnt = 0
            flag = False

        elif i == '(':
            stack.append(i)
        elif i == '{':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return "Compile Error"
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return "Compile Error"
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return "Compile Error"
    return "No Error"

x = ""
for line in sys.stdin:
    x += line.rstrip()

print(check(x))