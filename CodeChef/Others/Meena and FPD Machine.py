# Question Link
# https://www.codechef.com/CDKR2022/problems/FPDMACHINE

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

def solve(n,k,arr):
    ans = 0
    if arr[k-1]:
        ans = 1
    
    k -= 1
    l,r = k-1,k+1
    while  l >= 0 or r < n:
        if l >= 0 and r < n:
            if arr[l] and arr[r]:
                ans += 2

        elif l >= 0:
            if arr[l]:
                ans += 1

        relif r < n:
            if arr[r]:
                ans += 1

        l -= 1
        r += 1

    print(ans)

for _ in range(int(input())):
    n,k = get_int()
    arr = int_arr()
    solve(n,k,arr)
