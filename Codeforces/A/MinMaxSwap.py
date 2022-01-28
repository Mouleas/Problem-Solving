# Question Link
# https://codeforces.com/contest/1631/problem/A

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

def solve(n,a,b):
    for i in range(n):
        if b[i] < a[i]:
            a[i],b[i] = b[i],a[i]

    print(max(a)*max(b))
    
for _ in range(int(input())):
    n  = int(input())
    a = int_arr()
    b = int_arr()
    solve(n,a,b)
