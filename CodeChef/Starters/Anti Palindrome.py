# Question Link
# https://www.codechef.com/START24B/problems/ANTI_PAL

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

def solve():
    n = int(input())
    s = str(input())
    d = defaultdict(int)
    if n % 2 == 1:
        print("NO")
        return
    for i in range(len(s)):
        d[s[i]] += 1
        if d[s[i]] > n//2:
            print("NO")
            return

    s = list(s)
    s = sorted(s)
    l,r = 0,n-1
    x = 0
    while l < r:
        if s[l] == s[r]:
            s[x],s[l] = s[l],s[x]
            x += 1
        l += 1
        r -= 1 

    print("YES")
    print("".join(s))

T = 1
T = int(input())
while T:
    solve()
    T -= 1
