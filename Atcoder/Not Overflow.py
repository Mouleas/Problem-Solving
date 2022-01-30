# Question Link
# https://atcoder.jp/contests/abc237/tasks/abc237_a

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

def solve():pass

# for _ in range(int(input())):
n  =int(input())
if n >= -2**31 and n <= 2**31-1:
    print("Yes")
else:
    print("No")
