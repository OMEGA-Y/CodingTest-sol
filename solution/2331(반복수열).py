A, P = map(int,input().split())

data = set([A])
repeat = set([])
for _ in range(10000):
    rem = 0
    while A:
        rem += (A%10)**P
        A = int(A/10)
    A = rem

    if A in data:
        repeat.add(A)
    data.add(A)

print(len(data-repeat))

'''
일정 수부터 규칙적으로 반복되는 반복수열 같다.
랜덤으로 같은 숫자가 반복적으로 만들어진다는 줄 알고 set을 두 개 만들어서 뺐는데 
다른 사람들은 index로 접근해서 반복되는 숫자가 나오는 즉시, 그 때의 index 값을 출력하고 종료했다.
'''