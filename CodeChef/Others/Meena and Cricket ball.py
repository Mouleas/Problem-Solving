# Question Link
# https://www.codechef.com/CDKR2022/problems/MACBALL

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


for _ in range(int(input())):
    x,n,b = get_int()
    arr = sorted(int_arr())
    tot = 0
    for i in range(n):
        if x-arr[i] >= b:
            tot += 1
            x -= arr[i]
        else:
            break

    print(tot)
