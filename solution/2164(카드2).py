from collections import deque
N = int(input())

if N==1:
    print(1)
else:
    q = deque([i for i in range(1,N+1)])

    while len(q) != 1:
        q.popleft()
        q.append(q.popleft())

    print(q[0])

'''
list에 직접 원소를 넣고 빼고 하면 시간이 오래 걸릴거 같아서 규칙을 찾아서 푸는 문제인 줄 알았는데....
올바른 규칙을 찾지 못해 deque로 원소를 하나씩 넣고 빼고 했다.

다른 사람 풀이 보니까 규칙 찾은 분이 있다.
블로그를 통해 규칙을 어떻게 발견했는지 읽어봤는데,
입력과 출력을 순서대로 18정도까지 나열해보면 출력이 2,2,4,2,4,6,8,2,4,6,8,10,12,14,16,2,4,...
이런 식으로 반복이 되고 2의 제곱수는 모두 2의 제곱수가 그대로 출력된다.
그 사이에서 규칙을 찾아낸 것 같은데 쉽지는 않은 것 같다.

- 다른 사람 풀이
n,m=int(input()),1
while m<n:
    m*=2
print(n*2-m)
'''