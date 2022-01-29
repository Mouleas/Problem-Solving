# Question Link
# https://www.codechef.com/CDKR2022/problems/CATJUMP

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
    dp = [0 for i in range(n)]
    for i in range(1,n):
        minn = float("inf")
        for j in range(1,k+1):
            if i-j >= 0:
                tmp = dp[i-j]+abs(arr[i]-arr[i-j])
                minn = min(tmp,minn)
        dp[i] = minn

    print(dp[n-1])


for _ in range(int(input())):
    n,k = get_int()
    arr = int_arr()
    solve(n,k,arr)
