# Question Link
# https://www.codechef.com/CDKR2022/problems/SOURCECODE

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

def solve(number,n):
    for i in range(n-1,0,-1):
        if number[i] > number[i-1]:
            break

    if i == 1 and number[i] <= number[i-1]:
        print(-1)
        return
          
    x = number[i-1]
    smallest = i
    for j in range(i+1,n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j

    number[smallest],number[i-1] = number[i-1], number[smallest]
      
    x = 0
    for j in range(i):
        x = x * 10 + number[j]

    number = sorted(number[i:])
    for j in range(n-i):
        x = x * 10 + number[j]

    if x > 2**31-1 or x < -2**31:
        print(-1)
    else:
        print(x)

for _ in range(int(input())):
    n = str(input())
    lis = []
    for i in range(len(n)):
        lis.append(int(n[i]))
    solve(lis,len(n))
