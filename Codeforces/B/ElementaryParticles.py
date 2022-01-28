# Question Link
# https://codeforces.com/contest/1625/problem/B
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
    d = defaultdict(list)
    for i in range(n):
        d[arr[i]].append(i)

    maxx = -1
    for i in d:
        if len(d[i]) >= 2:
            tmp = d[i]
            for j in range(1,len(tmp)):
                maxx = max(((n-tmp[j])+tmp[j-1]),maxx)

    print(maxx)

for _ in range(int(input())):
    n  = int(input())
    arr = int_arr()
    solve(n,arr)
