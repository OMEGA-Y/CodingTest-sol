import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    word, *num = list(input().strip().split())
    if word == 'push':
        queue.append(num[0])
    elif word == 'size':
        print(len(queue))
    elif word == 'pop':
        if queue:
            m = queue.pop(0)
            print(m)
        else:
            print(-1)
    elif word == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif word == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)