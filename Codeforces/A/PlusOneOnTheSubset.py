# Question Link
# https://codeforces.com/contest/1624/problem/A

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

def solve(n,arr):
    maxx = arr[-1]
    c = 0
    for i in range(n):
        c = max(maxx-arr[i],c)

    print(c)
    
for _ in range(int(input())):
    n = int(input())
    arr = int_arr()
    arr.sort()
    solve(n,arr)
