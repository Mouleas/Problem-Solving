# Question Link
# https://atcoder.jp/contests/abc237/tasks/abc237_d

import sys
from math import sqrt,ceil,floor,gcd
from collections import Counter,defaultdict,deque

def int_arr(): return list(map(int,input().split()))
def str_arr(): return list(map(str,input().split()))
def get_str(): return map(str,input().split())
def get_int(): return map(int,input().split())
def get_flo(): return map(float,input().split())
def lcm(a,b): return (a*b) // gcd(a,b)

mod = 1000000007

def solve(n,s):
    prev = -1
    tmp = ""
    for i in range(n-1,-1,-1):
        if prev == -1:
            tmp += s[i]
            prev = s[i]
        else:
            if s[i] == prev:
                if s[i] == "L":
                    tmp += "R"
                else:
                    tmp += "L"
            else:
                tmp += s[i]

            prev = s[i]

    tmp = tmp[::-1]

    A = deque()
    for i in range(n-1,-1,-1):
        if i == n-1:
            A.appendleft(i+1)
        else:
            if tmp[i] == "L":
                A.appendleft(i+1)
            else:
                A.append(i+1)


    if s[0] == "L":
        A.append(0)
    else:
        A.appendleft(0)

    while A:
        val = A.popleft()
        print(val,end=" ")

# for _ in range(int(input())):
n = int(input())
s = str(input())
solve(n,s)
