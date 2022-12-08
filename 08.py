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


def solve(lst):
	r = 0
	s = set()
	d = {}
	root = Node(0, '/', True, None)
	root.parent = root
	cur = root
	m = [[int(c) for c in l] for l in lst]
	# for i in range(len(m)):
	# 	max_h = -1
	# 	for j in range(len(m[i])):
	# 		if m[i][j] > max_h:
	# 			s.add((i, j))
	# 		max_h = max(m[i][j], max_h)
	# 	max_h = -1
	# 	for j in range(len(m[i]) - 1, -1, -1):
	# 		print(i, j, m[i][j], max_h)
	# 		if m[i][j] > max_h:
	# 			s.add((i, j))
	# 		max_h = max(m[i][j], max_h)
	# for j in range(len(m[0])):
	# 	max_h = -1
	# 	for i in range(len(m)):
	# 		# print(i, j, m[i][j], max_h)
	# 		if m[i][j] > max_h:
	# 			s.add((i, j))
	# 		max_h = max(m[i][j], max_h)
	# 	max_h = -1
	# 	for i in range(len(m) - 1, -1, -1):
	# 		if m[i][j] > max_h:
	# 			s.add((i, j))
	# 		max_h = max(m[i][j], max_h)
	for i in range(len(m)):
		for j in range(len(m[0])):

			u, d, ri, le = 0, 0,0, 0 
			for up in range(1, i + 1):
				u += 1
				if m[i - up][j] < m[i][j]:
					continue
				else:
					break
			for down in range(1, len(m) - i):
				d += 1
				if m[i + down][j] < m[i][j]:
					continue
				else:
					break
			for right in range(1, j + 1):
				ri +=1
				if m[i][j - right] < m[i][j]:
					continue
				else:
					break
			for left in range(1, len(m[0]) - j):
				le += 1
				if m[i][j + left] < m[i][j]:
					continue
				else:
					break
			# print(i, j, u, d, ri, le)
			r = max(r, u * d * ri * le)

	# r = len(s)
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
