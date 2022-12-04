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

def solve(lst):
	r = 0
	n = 3
	d = defaultdict(int)

	for l in lst:
		s = l.split(',')
		x = [[int(i) for i in p.split('-')] for p in s]
		
		# if x[0][0] <= x[1][0] and x[0][1] >= x[1][1] or x[0][0] >= x[1][0] and x[0][1] <= x[1][1]:
		# 	r += 1
		if x[0][0] <= x[1][1] and x[0][1] >= x[1][0]:
			print(x)
			r += 1
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
