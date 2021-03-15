import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    res = input().rstrip()
    score = 0
    cnt = 1
    for i in range(len(res)):
        if res[i] == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)