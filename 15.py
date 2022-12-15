import re
import pyperclip
from collections import defaultdict, deque
import tqdm
import math
import z3
import heapq
from itertools import permutations, product
import numpy as np
import copy
import random
from functools import reduce, cmp_to_key
from operator import mul

def process(filename):
	f = open(filename, 'r')
	content = f.read()

	return content.splitlines()


def solve(lst):
	r = 0
	s = set()
	d = defaultdict(int)
	max_x = 0
	min_x = 999999999999
	max_d = 0
	r_s = set()
	for l in lst:
		l = [int(c) for c in re.findall(r'-?\d+', l)]
		s_x, s_y, b_x, b_y = l[0], l[1], l[2], l[3]
		m_d = abs(s_x - b_x) + abs(s_y - b_y)
		d[(s_x, s_y)] = m_d
		s.add((b_x, b_y))

		max_d = max(m_d, max_d)
		min_x = min(min(min_x, b_x), s_x)
		max_x = max(max(max_x, b_x), s_x)
	print(d)

	# for b_x in tqdm.tqdm(range(min_x - max_d - 999999, max_x + max_d + 999999)):
	# 	b_y = 2000000
	# 	# b_y = 10
	# 	f = False
	# 	for s_x, s_y in d:
	# 		m_d = abs(s_x - b_x) + abs(s_y - b_y)
	# 		if m_d == d[(s_x, s_y)]:
	# 			print(s_x, s_y, b_x, b_y, m_d)
	# 		# print(m_d, d[(s_x, s_y)])
	# 		if (b_x, b_y) not in r_s and m_d <= d[(s_x, s_y)] and (b_x, b_y) not in s:
	# 			r_s.add((b_x, b_y))
	# 			break
		# if not f:
		# 	print(b_x, b_y)
	# for s_x, s_y in d:
	# 	m_d = d[(s_x, s_y)]
	# 	b_y = 2000000
	# 	# b_y = 10
	# 	for b_x in range(s_x - max_d, s_x + max_d + 1):
	# 		if (b_x, b_y) not in r_s and (abs(s_x - b_x) + abs(s_y - b_y)) <= m_d and (b_x, b_y) not in s:
	# 			r_s.add((b_x, b_y))

	# for x in tqdm.tqdm(range(4000000)):
	# 	for y in range(4000000):
	# 		f = True
	# 		for s_x, s_y in d:
	# 			m_d = abs(s_x - b_x) + abs(s_y - b_y)
	# 			if m_d <= d[(s_x, s_y)]:
	# 				f = False
	# 				break
	# 		if f:
	# 			return 4000000 * x + y
	s = z3.Solver()
	x = z3.Int("x")
	y = z3.Int("y")
	s.add(0 <= x)
	s.add(x <= 4000000)
	s.add(0 <= y)
	s.add(y <= 4000000)
	for s_x, s_y in d:
		m = d[(s_x, s_y)]
		s.add(zabs(s_x - x) + zabs(s_y - y) > m)
	print(s.check())
	print(s.model())
	# return len(r_s)
	return 2889465 * 4000000 + 3040754

def zabs(x):
    return z3.If(x >= 0, x, -x)

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
