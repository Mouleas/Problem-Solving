# Question Link
# https://codeforces.com/contest/1624/problem/B

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

def solve(a,b,c):
    d1,d2 = a-b,b-c
    if len(set([a,b,c])) == 1:
        print("YES")
    elif (d1 == d2) or ((2*b-c)%a == 0 and 2*b-c > 0) or ((a+c)%(2*b) == 0) or ((2*b-a)%c == 0 and 2*b-a>0):
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    a,b,c = get_int()
    solve(a,b,c)
