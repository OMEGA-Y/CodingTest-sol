import sys

a, b = 0, 0
num_list = [int(i.rstrip()) for i in sys.stdin]

N = 1000000
nums = [False,False] + [True] * (N-1)
for i in range(2, int(N**0.5 + 1.5)):
    if nums[i]: #True
        nums[i*2::i] = [False] * ((N-i)//i)

prime = [i for i in range(3,N) if nums[i]==True]

for num in num_list:
    if num==0:
        break
    for i in prime:
        if nums[num-i]:
            a = i
            b = num-i
            break

    if a:
        print(f'{num} = {a} + {b}')
    else:
        print("Goldbach's conjecture is wrong.")


'''소수 구하는 방법 - 에라토스테네스의 체(set 이용)
prime = set([i for i in range(3, N, 2)])
for i in range(3, N, 2):
    if i in prime:
        prime -= set([i for i in range(i * 2, N, i)])   # list끼리 (-) 연산 불가능하므로 set 이용

prime = list(prime)
prime.sort()
'''

'''소수 구하는 방법 - 에라토스테네스의 체(True,False 이용)
nums = [False,False] + [True] * (N-1)
for i in range(2, int(N**0.5)+1):
    if nums[i]: #True
        nums[i*2::i] = [False] * ((N-i)//i)

prime = [i for i in range(2,N) if nums[i]==True] # 이 문제를 풀 때는 3부터 prime에 담았다.
'''

'''처음 접근 방법
for num in num_list:
    if num==0:
        break
    for i in prime:
        if num-i in prime:
            a = i
            b = num-i
            break
            
여기서 if num-i in prime은 prime 리스트를 쭉 훑어 보면서 num-i가 있는지 검사한다.
매우 비효율적인 방법이라 계속 시간초과가 났다...
배열의 인덱스라 접근하는 방법으로 바꿨더니 풀렸다!
'''