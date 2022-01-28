# Question link
# https://codeforces.com/contest/1629/problem/A

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

def solve(n,k,a,b):
    tmp = []
    for i in range(n):
        tmp.append([a[i],b[i]])

    tmp.sort(key =lambda x:x[0])

    for i in range(n):
        if tmp[i][0] <= k:
            k += tmp[i][1]

    print(k)

for _ in range(int(input())):
    n,k  = get_int()
    a = int_arr()
    b = int_arr()
    solve(n,k,a,b)
