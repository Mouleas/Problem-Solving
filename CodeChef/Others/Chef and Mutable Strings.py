# Question Link
# https://www.codechef.com/CBND2022/problems/CHEFSTR22

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

def solve():
	s = str(input())
	t = str(input())
	if len(s) != len(t):
		print("No")
		return
	for i in range(len(s)):
		if s[i] != t[i]:
			if s[i] in list("aeiou"):
				if t[i] not in list("aeiou"):
					print("No")
					return

			else:
				if t[i] in list("aeiou"):
					print("No")

	print("Yes")

T = 1
# T = int(input())
while T:
    solve()
    T -= 1
