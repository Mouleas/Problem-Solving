# Question Link
# https://codeforces.com/contest/1617/problem/A

import sys
from math import sqrt,ceil,floor,gcd
from collections import Counter,defaultdict

def int_arr(): return list(map(int,input().split()))
def str_arr(): return list(map(str,input().split()))
def get_str(): return map(str,input().split())
def get_int(): return map(int,input().split())
def get_flo(): return map(float,input().split())
def lcm(a,b): return (a*b) // gcd(a,b)

mod = 1000000007

def solve(s,t):
    t = list(t)
    d = defaultdict(int)
    for i in s:
        d[i] += 1

    tmp = []
    for i in d:
        tmp.append(i)

    tmp.sort()

    if len(tmp) >= 3:
        if tmp[1] == t[1] and tmp[2] == t[2]:
            tmp[1],tmp[2] = tmp[2],tmp[1]

    ans = ""
    for i in tmp:
        ans += i*d[i] 

    print(ans)

for _ in range(int(input())):
    s = str(input())
    t = str(input())
    solve(s,t)
