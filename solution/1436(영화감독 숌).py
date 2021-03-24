def count(N):
    cnt = 0
    for i in range(666,3000000):
        if str(i).find('666') != -1:
            cnt += 1
        if cnt == N:
            return i

N = int(input())
print(count(N))

# 완전탐색(브루트포스 알고리즘) 문제이다.
# 규칙 찾아서 효율적으로 풀어보려 했으나.. 너무 피곤하다.
# 맞은 사람 풀이 보니까 규칙 찾으신 분들도 있던데 이해를 못하겠다..