# Question Link
# https://codeforces.com/contest/1631/problem/B

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
    i = n-2
    tot = 0
    while i >= 0 and i <= n-1:
        if arr[i] == arr[-1]:
            i -= 1
        else:
            i -= (n-i-1)
            tot += 1
    print(tot)

for _ in range(int(input())):
    n = int(input())
    arr = int_arr()
    solve(n,arr)
