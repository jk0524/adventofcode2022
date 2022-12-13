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
	# return content.split('\n\n')

def compare(left, right):
	if type(left) == int and type(right) == int:
		if left < right:
			return 'right'
		if left > right:
			return 'bad'
		return 'not'
	if type(left) == int:
		left = [left]
	if type(right) == int:
		right = [right]
	for i in range(min(len(left), len(right))):
		c = compare(left[i], right[i])
		if c == 'right' or c == 'bad':
			return c
	if len(left) == len(right):
		return 'not'
	if len(left) < len(right):
		return 'right'
	return 'bad'

def cmp_f(left, right):
	if compare(left, right) == 'right':
		return -1
	return 1
def solve(lst):
	r = 1
	s = set()
	d = {}
	i = 1
	# for l in lst:
	# 	l = l.splitlines()
	# 	left, right = eval(l[0]), eval(l[1])
	# 	if i == 3:
	# 		print(left, right)
	# 	if compare(left, right) == 'right':
	# 		print(i)
	# 		r += i
	# 	i += 1
	packets = [eval(l) for l in lst if l] 
	packets.append([[2]])
	packets.append([[6]])
	p = sorted(packets, key=cmp_to_key(cmp_f))
	r = 1
	for i in range(len(p)):
		if p[i] == [[2]]:
			r *= (i + 1)
		if p[i] == [[6]]:
			r *= (i + 1)
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
