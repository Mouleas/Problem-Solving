# Question Link
# https://codeforces.com/contest/1624/problem/C

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
    d = defaultdict(int)
    for i in range(n):
        d[i+1] = 0

    for i in range(n):
        while arr[i] > n:
            arr[i] = int(arr[i]/2)
        d[arr[i]] += 1

    for i in d:
        while d[i] > 1:
            ok = 0
            tmp = i
            while tmp > 0:
                if d[tmp] == 0:
                    d[tmp] += 1
                    ok = 1
                    break
                else:
                    tmp = int(tmp/2)

            if not ok:
                print("NO")
                return
            d[i] -= 1

    for i in d:
        if d[i] == 0:
            print("NO")
            return

    print("YES")

for _ in range(int(input())):
    n = int(input())
    arr = int_arr()
    solve(n,arr)
