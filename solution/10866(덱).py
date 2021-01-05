import sys
input = sys.stdin.readline

queue = []
for _ in range(int(input())):
    word, *num = input().strip().split()
    if word == 'push_front':
        queue.insert(0,num[0])
    elif word == 'push_back':
        queue.append(num[0])
    elif word == 'size':
        print(len(queue))
    elif word == 'pop_front':
        if queue:
            m = queue.pop(0)
            print(m)
        else:
            print(-1)
    elif word == 'pop_back':
        if queue:
            m = queue.pop()
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
    elif word == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)