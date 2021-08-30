# 내 풀이
def solution(price, money, count):
    p = 0
    for i in range(1,count+1):
        p += i*price
    if p-money <=0:
        return 0
    else:
        return p-money

# 추천된 풀이 (산술평균.. 대박)
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)