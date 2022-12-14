import re
import pyperclip
from collections import defaultdict, deque
import tqdm
import math
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

def drop(d, max_y):
	x, y = 500, 0
	while y <= max_y:
		if not d[(x, y + 1)] and not y == max_y - 1:
			y += 1
		elif not d[(x - 1, y + 1)]and not y == max_y - 1:
			x -= 1
			y += 1
		elif not d[(x + 1, y + 1)] and not y == max_y - 1:
			x += 1
			y += 1
		else:
			d[(x, y)] = 1
			return x, y
	return None

def solve(lst):
	r = 0
	s = set()
	d = defaultdict(int)
	max_y = 0
	for l in lst:
		path = [eval(c) for c in l.split(' -> ')]
		for i in range(len(path) - 1):
			start_x, start_y = path[i]
			end_x, end_y = path[i + 1]
			for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
				for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
					d[(x, y)] = 1
					max_y = max(y, max_y)
	print(d)

	while True:
		# if drop(d, max_y):
		# 	r += 1
		# else:
		# 	return r
		r += 1
		if drop(d, max_y + 2) == (500, 0):
			return r



	
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
