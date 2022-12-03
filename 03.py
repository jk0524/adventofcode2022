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

def process(filename):
	f = open(filename, 'r')
	content = f.read()

	return content.splitlines()

def val(c):
	if c.islower():
		return ord(c) - ord('a') + 1
	return ord(c) - ord('A') + 27

def solve(lst):
	r = 0
	n = 3
	d = defaultdict(int)

	# for l in lst:
	# 	f, s = l[len(l) // 2:], l[:len(l) // 2]
	# 	print(f, s)
	# 	for c in f:
	# 		if c in s:
	# 			r += val(c)
	# 			break
	groups = [lst[i:i + n] for i in range(0, len(lst), n)]
	for g in groups:
		for c in g[0]:
			if c in g[1] and c in g[2]:
				r += val(c)
				break

	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
