import sys
input = sys.stdin.readline

def find(num):
    for i in list(str(num)):
        if broke[int(i)]:
            return -1
    return len(str(num))

N = int(input().rstrip())
M = int(input().rstrip())
broke = [0]*10

if N == 100:
    print(0)
else:
    if M:
        for i in map(int,input().split()):
            broke[i] = 1

    minCnt = abs(N-100)

    tmp = 0
    for i in range(1000001):
        keyLen = find(i)

        if keyLen != -1:
            tmp = keyLen+abs(i-N)
            minCnt = min(tmp,minCnt)


    print(minCnt)

'''풀이
1. +,- 만 눌러서 목표 채널에 도달하는 방법
2. 숫자 버튼을 이용해 N에 가까운 채널로 이동한 후, + 또는 - 버튼을 눌러 목표 채널에 도달하는 방법
3. 숫자 버튼만 눌러서 목표 채널에 도달하는 방법

세 가지 경우 중 최솟값을 출력한다.

숫자버튼을 눌러 갈 수 있는 채널의 범위는 0~1,000,000으로 제한한다.
왜냐하면 N이 0~500,000 사이의 수이기 때문이다.
N의 최댓값인 500,000을 가는 경우에 1,000,000보다 큰 숫자로 이동 후, -버튼을 누를거면
현재 채널 값(100)에서 +버튼을 눌러서 원하는 채널로 이동하는게 무조건 이동 횟수의 최솟값이 된다.
'''