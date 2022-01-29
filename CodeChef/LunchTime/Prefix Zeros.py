# Question Link
# https://www.codechef.com/LTIME104B/problems/PREZ

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

def solve(n,k,s):
    ans = -1
    l = 0
    r = n-1
    arr = [int(i) for i in s]
    while l <= r:
        mid = l+(r-l)//2
        tmp = 0
        A = arr.copy()
        for i in range(mid,-1,-1):
            if (A[i]+tmp)%10 == 0 or (i == mid and A[i]== 0):
                continue
            else:
                A[i] += tmp
                A[i] = A[i]%10
                tmp += (10-A[i])
                
                if tmp > k:
                    r = mid-1
                    break

        if tmp <= k:
            ans = max(mid,ans)
            l = mid+1

    print(ans+1)

for _ in range(int(input())):
    n,k = get_int()
    s = str(input())
    solve(n,k,s)
