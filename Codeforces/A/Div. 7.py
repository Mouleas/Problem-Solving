# Question Link
# https://codeforces.com/contest/1633/problem/A

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

def solve(n):
    n = str(n)
    if int(n) % 7 == 0:
        print(n)
        return
    for i in range(0,10):
        if int(n[:-1]+str(i))%7 == 0:
            print(n[:-1]+str(i))
            return
    
for _ in range(int(input())):
    n = int(input())
    solve(n)
