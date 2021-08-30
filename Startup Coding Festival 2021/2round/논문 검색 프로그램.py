# 결국 못 풀었음. 시간초과 문제로 예상.
import sys
from collections import defaultdict
input = sys.stdin.readline

def cal(dict,index,w):
    if dict[w[0]]:
        for i in dict[w[0]]:
            if i+len(w) > len(index):
                continue
            if index[i:i+len(w)] == w:
                return True
    return False

s = []
s_dict = []
N = int(input())
for _ in range(N):
    w = input().rstrip()
    s.append(w)
    tmp = defaultdict(list)
    for idx,val in enumerate(w):
        tmp[val].append(idx)
    s_dict.append(tmp)

q = []
Q = int(input())
for _ in range(Q):
    w = input().rstrip()
    q.append(w)

cnt = [0]*Q
for idx,dict in enumerate(s_dict):
    for j,w in enumerate(q):
        if len(w) > len(s[idx]):
            continue
        if w == s[idx] or cal(dict,s[idx],w):
            cnt[j] += 1

for c in cnt:
    print(c)