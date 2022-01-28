# Question Link
# https://codeforces.com/contest/1625/problem/A

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
    ans = ""
    length = 0
    tmp = []
    for i in range(n):
        bb = bin(arr[i]).replace("0b","")
        tmp.append(bb)
        length = max(len(bb),length)
    
    for i in range(length):
        o,z = 0,0
        for j in tmp:
            if len(j) < length:
                j = "0"*(length-len(j))+j
            if j[i] == "1":
                o += 1
            else:
                z += 1
        if o > z:
            ans += "1"
        else:
            ans += "0"

    print(int(ans,2))


for _ in range(int(input())):
    n,l = get_int()
    arr = int_arr()
    solve(n,l,arr)
    
