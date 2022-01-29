# Question Link
# https://www.codechef.com/CDKR2022/problems/RAMPUP

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
    ans = -1
    d = defaultdict(int)
    for i in range(n):
        d[arr[i]] += 1
    
    for i in range(n-1):
        for j in range(i+1,n):
            diff = arr[j]-arr[i]
            tmp = arr[j]
            c = 2
            while diff+tmp in d:
                tmp += diff
                c += 1
            ans = max(c,ans)

    print(ans)
    
for _ in range(int(input())):
    n = int(input())
    arr = int_arr()
    solve(n,arr)    
