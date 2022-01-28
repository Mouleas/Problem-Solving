# Question Link
# https://codeforces.com/contest/1627/problem/A

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

def solve(n,m,x,y,arr):
    x -= 1
    y -= 1
    if arr[x][y] == "B":
        print(0)
        return

    col = False
    for i in range(n):
        if arr[i][y] == "B":
            col = True

    row = False
    for i in range(m):
        if arr[x][i] == "B":
            row = True

    if row or col:
        print(1)
        return
    
    else:
        row = False
        for i in range(n):
            if "B" in arr[i]:
                row = True
                print(2)
                return

        print(-1)

for _ in range(int(input())):
    n,m,x,y = get_int()
    arr = []
    for i in range(n):
        arr.append(list(str(input())))
    solve(n,m,x,y,arr)
