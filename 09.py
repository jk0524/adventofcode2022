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
	# return content.split('\n\n')

class Node:
	def __init__(self, size, name, is_folder, parent):
		self.size = size
		self.name = name
		self.is_folder = is_folder
		self.children = []
		self.parent = parent

	def total_size(self):
		if self.is_folder:
			return sum([n.total_size() for n in self.children])
		return self.size

	def all_folders(self):
		if self.is_folder:
			lst = [self]
			for n in self.children:
				lst.extend(n.all_folders())
			return lst
		return []

def clip(x):
	if x > 0:
		return 1
	if x < 0:
		return -1
	return 0

def move(hi, hj, ti, tj):
	di = hi - ti
	dj = hj - tj
	if abs(di) < 2 and abs(dj) < 2:
		return ti, tj
	return ti + clip(di), tj + clip(dj)

def solve(lst):
	r = 0
	s = set()
	d = {}
	# root = Node(0, '/', True, None)
	# root.parent = root
	# cur = root
	hi, hj = 0, 0
	ti, tj = 0, 0
	# s.add((ti, tj))
	# for l in lst:
	# 	l = l.split(' ')
	# 	di, val = l[0], int(l[1])
	# 	for _ in range(val):
	# 		if di == 'L':
	# 			hi -= 1
	# 		elif di == 'R':
	# 			hi += 1
	# 		elif di == 'U':
	# 			hj += 1
	# 		else:
	# 			hj -= 1
	# 		ti, tj = move(hi, hj, ti, tj)
	# 		print(hi, hj, ti, tj)
	# 		s.add((ti, tj))
	rope = [(0,0) for i in range(10)]
	for l in lst:
		l = l.split(' ')
		di, val = l[0], int(l[1])

		for _ in range(val):
			for i in range(10):
				hi, hj = rope[i]
				if i == 0:
					if di == 'L':
						hi -= 1
					elif di == 'R':
						hi += 1
					elif di == 'U':
						hj += 1
					else:
						hj -= 1
					rope[i] = hi, hj
				else:
					hi, hj = rope[i - 1]
					ti, tj = rope[i]
					ti, tj = move(hi, hj, ti, tj)
					rope[i] = ti, tj
					if i == 9:
						s.add((ti, tj))
	print(s)

	r = len(s)
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
