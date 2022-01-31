# Question Link
# https://codeforces.com/contest/1632/problem/B

import sys
from math import sqrt,ceil,floor,gcd,log
from collections import Counter,defaultdict

def int_arr(): return list(map(int,input().split()))
def str_arr(): return list(map(str,input().split()))
def get_str(): return map(str,input().split())
def get_int(): return map(int,input().split())
def get_flo(): return map(float,input().split())
def lcm(a,b): return (a*b) // gcd(a,b)

mod = 1000000007

def solve(n):
    p = pow(2,int(log(n-1)/log(2)))
    for i in range(1,n):
        if i == p:
            print("0",end=" ")
            print(i,end=" ")
        else:
            print(i,end=" ")
    print()
    
for _ in range(int(input())):
    n = int(input())
    solve(n)
