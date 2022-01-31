# Question Link
# https://codeforces.com/contest/1633/problem/B

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
    o,z = 0,0
    for i in range(len(s)):
        if s[i] == "1":
            o += 1
        else:
            z += 1

    if o == z:
        print(o-1)
    else:
        print(min(o,z))

for _ in range(int(input())):
    s = str(input())
    solve(s)
