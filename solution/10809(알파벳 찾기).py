import sys
input = sys.stdin.readline

list = [-1]*26

for idx,val in enumerate(input().rstrip()):
    chr = ord(val)-ord('a')
    if list[chr] == -1:
        list[chr] = idx

print(*list)