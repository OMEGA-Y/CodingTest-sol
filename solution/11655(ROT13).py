import sys

data = sys.stdin.readline().rstrip()
output = ""
for i in data:
    if i.islower():
        output += chr(97+int((ord(i)-ord('a')+13)%26))
    elif i.isupper():
        output += chr(65+int((ord(i)-ord('A')+13)%26))
    else:
        output += i

print(output)