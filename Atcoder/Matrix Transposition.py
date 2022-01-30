# Question Link
# https://atcoder.jp/contests/abc237/tasks/abc237_b

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

def solve(x,y,s):
    B = [[0 for X in range(x)] for Y in range(y)]

    for i in range(y):
        for j in range(x):
            B[i][j] = A[j][i]

    for i in B:
        print(*i)
        
# for _ in range(int(input())):
x,y = get_int()
A = []
for i in range(x):
    A.append(int_arr())

solve(x,y,A)
