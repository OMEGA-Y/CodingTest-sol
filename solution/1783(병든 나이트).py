import sys
input = sys.stdin.readline

def knight(N,M):
    if N == 1 or M == 1:
        return 1
    else:
        if N < 3:
            if M == 2:
                return 1
            if M == 3 or M == 4:
                return 2
            if M == 5 or M == 6:
                return 3
            if M >= 7:
                return 4
        else:
            if M < 7:
                return min(M,4)
            else:
                return M-2  # 5(이동방법 모두 한 번씩 사용)+M-7(이동방법 3개를 최소 한 번씩 사용할 수 있는 M의 최솟값)

N,M = map(int, input().split())
print(knight(N,M))
