# Question link
# https://codeforces.com/contest/1629/problem/B

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

for _ in range(int(input())):
    l,r,k = get_int()

    rem = r-l

    ans = (r - l) // 2
    
    if (r % 2 != 0 or l % 2 != 0):
        ans += 1

    if l == r and l > 1:
        print("YES")
 
    elif ans <= k:
        print("YES")
    else:
        print("NO")
