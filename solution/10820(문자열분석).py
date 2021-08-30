import sys

for line in sys.stdin:
    up, lo, sp, nu = 0, 0, 0, 0
    for l in line.strip('\n'):
        if l.isupper():
            up += 1
        elif l.islower():
            lo += 1
        elif l.isdigit():
            nu += 1
        elif l.isspace():
            sp += 1
    sys.stdout.write(f"{lo} {up} {nu} {sp}\n")

'''내가 짠 코드
for line in sys.stdin:
    print(sum(map(int,map(line.count,map(chr,range(97,123))))), end=" ")
    print(sum(map(int,map(line.count,map(chr,range(65,91))))), end=" ")
    print(sum(map(int,map(line.count,map(chr,range(48,58))))),end=" ")
    print(line.count(" "))
'''