import sys

def palindrome(num):
    l = len(num)
    for i in range(0,l//2):
        if num[i] != num[l-i-1]:
            return 'no'
    return 'yes'

for line in sys.stdin:
    if line.rstrip() == '0':
        break
    print(palindrome(line.rstrip()))