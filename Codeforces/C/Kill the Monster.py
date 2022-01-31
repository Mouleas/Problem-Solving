# Question Link
# https://codeforces.com/contest/1633/problem/C

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

def solve(hc,ac,hm,am,k,h,a):
    char_Acc = ceil(hm/ac)
    mon_Acc = ceil(hc/am)
    if char_Acc <= mon_Acc:
        print("YES")
        return
    for i in range(k+1):
        HC = hc+(i*a)
        AC = ac+((k-i)*h)
        char_Acc = ceil(hm/AC)
        mon_Acc = ceil(HC/am)
        if char_Acc <= mon_Acc:
            print("YES")
            return

    print("NO") 

for _ in range(int(input())):
    hc,ac = get_int()
    hm,am = get_int()
    k,h,a = get_int()
    solve(hc,ac,hm,am,k,h,a)
