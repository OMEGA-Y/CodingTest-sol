N = input()

if len(N)%3 == 1:
    N = '00' + N
elif len(N)%3 == 2:
    N = '0' + N

rem = ""
for i in range(int(len(N)/3)):
    sub = N[3*i:3*(i+1)]
    rem += str(int(sub,2))

if rem:
    print(rem)
else:
    print(0)


'''다른 사람 풀이
print(oct(int(input(),2))[2:])
'''