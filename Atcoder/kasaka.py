# Question Link
# https://atcoder.jp/contests/abc237/tasks/abc237_c

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

def solve(s):
    if s == s[::-1]:
        print("Yes")
    else:
        x,y = 0,0
        for i in range(len(s)):
            if s[i] == "a":
                x += 1
            else:
                break

        for j in range(len(s)-1,-1,-1):
            if s[j] == "a":
                y += 1
            else:
                break

        if x > y:
            print("No")
        else:
            diff = y-x
            l,r = 0,len(s)-diff
            if s[l:r] == s[l:r][::-1]:
                print("Yes")
            else:
                print("No")

# for _ in range(int(input())):
s = str(input())
solve(s)






