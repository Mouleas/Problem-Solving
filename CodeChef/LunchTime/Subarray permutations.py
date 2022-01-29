# Question Link
# https://www.codechef.com/LTIME104B/problems/SUBPERM

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

def solve(a,b):
    if a > 1 and b == 1:
        print(-1)
        return 
    ans = [i for i in range(1,a)]
    ans.insert(b-1,a)
    print(*ans)

for _ in range(int(input())):
    a,b = get_int()
    solve(a,b)
