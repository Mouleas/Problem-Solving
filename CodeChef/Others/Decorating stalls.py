# Question Link
# https://www.codechef.com/CDKR2022/problems/STADEC

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

def solve(n,k):pass

for _ in range(int(input())):
    a,b,c = get_int()
    minn = (a+b+c)//3
    A = sorted([a,b,c])
    print(min(minn,A[0]+A[1]))
