import sys

rem = set()
for line in sys.stdin:
    num = int(line.rstrip())
    rem.add(num%42)

print(len(rem))