# Question Link
# https://www.codechef.com/START24B/problems/ORANDCON

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

def solve():
    n = int(input())
    a = 0
    b = n
    c = "1"+bin(n).replace("0b","")
    c = int(c,2)
    print(a,b,c)

T = 1
T = int(input())
while T:
    solve()
    T -= 1
