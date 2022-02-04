# Question Link
# https://www.codechef.com/CBND2022/problems/CHEFERR

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
	n = int(input())
	prev = []
	for i in range(n):
		curr = int_arr()
		if prev == []:
			prev.append(curr)
		else:
			if abs(prev[-1][0]-curr[0]) <  abs(prev[-1][1]-curr[1]):
				print("NO")
				return 
			elif prev[-1][1] > curr[1]:
				print("NO")
				return

			elif prev[-1][0] >= curr[0]:
				if curr[0] == prev[-1][0] and prev[-1][1] != curr[1]:
					print("NO");return
				elif prev[-1][0] > curr[0]:
					print("NO");return

			prev.append(curr)

	per = (prev[-1][1]/prev[-1][0])*100
	if per < 25:
		print("YES HARD")
	elif per >= 25 and per < 50:
		print("YES MEDIUM")
	elif per >= 50 and per < 75:
		print("YES EASY")
	else:
		print("YES CAKEWALK")



T = 1
T = int(input())
while T:
    solve()
    T -= 1
