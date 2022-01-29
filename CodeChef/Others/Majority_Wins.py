# Question Link
# https://www.codechef.com/CDKR2022/problems/MEENA_008

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
    n = int(input())
    arr = int_arr()
    d = defaultdict(int)
    for i in range(n):
        d[arr[i]] += 1

    maxx = float("-inf")
    ele = -1
    for i in d:
        if d[i] > maxx:
            maxx = max(d[i],maxx)
            ele = i

    if maxx > n//2:
        print(ele)
    else:
        print("NOTA")
