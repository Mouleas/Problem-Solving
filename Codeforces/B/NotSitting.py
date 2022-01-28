# Question Link
# https://codeforces.com/contest/1627/problem/B
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

def solve(x,y):
    dp = []
    for i in range(x):
        for j in range(y):
            dp.append(max(i,x-i-1)+max(j,y-j-1))

    dp.sort()
    print(*dp)

for _ in range(int(input())):
    x,y = get_int()
    solve(x,y)
