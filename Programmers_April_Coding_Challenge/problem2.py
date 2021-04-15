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
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

def solution(s):
    if len(s)==1:
        return 0
    cnt = 0
    for i in range(len(s)):
        s = s+s[0]
        s = s[1:]
        if check(s):
            cnt += 1
    return cnt

print(solution("(("))