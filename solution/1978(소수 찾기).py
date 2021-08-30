input()
num = set(map(int,input().split()))

prime = set([i for i in range(3,max(num)+1,2)])
for i in range(3,max(num)+1,2):
    if i in prime:
        prime -= set([i for i in range(i*2,max(num)+1,i)])

prime.add(2)

print(len(num.intersection(prime)))