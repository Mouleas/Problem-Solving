# Question Link
# https://codeforces.com/contest/1626/problem/B

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

def solve(s):
    for i in range(len(s)-1,0,-1):
        if int(s[i-1])+int(s[i]) >= 10:
            tmp = int(s[i-1])+int(s[i])
            print("".join(s[:i-1])+str(tmp)+"".join(s[i+1:]))
            return

    tmp = 0
    if len(s) <= 2:
        for i in s:
            tmp += int(i)
        print(tmp)
        return
    tmp = int(s[0])+int(s[1])
    print(str(tmp)+"".join(s[2:]))

for _ in range(int(input())):
    s = list(str(input()))
    solve(s)
