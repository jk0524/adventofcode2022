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
from functools import reduce
from operator import mul

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

class Monkey:
	def __init__(self, m_string):
		self.cnt = 0
		for l in m_string.splitlines():
			if 'Operation' in l:
				self.f = l.split('= ')[1]
			elif l[:6] == 'Monkey':
				self.id = l.split(' ')[1][0]
				print(self.id)
			elif 'Starting items:' in l:
				self.items = [int(c) for c in l.split(': ')[1].split(', ')]
				print(self.items)
			elif 'Test:' in l:
				self.test_factor = int(l.split('divisible by ')[1])
				print(self.test_factor)
			elif 'If true' in l:
				self.true_target = l.split('throw to monkey ')[1]
				print(self.true_target)
			else:
				self.false_target = l.split('throw to monkey ')[1]
				print(self.false_target)
		self.cache = {}
	def inspect(self, old):
		self.cnt += 1
		return eval(self.f)

	def test(self, item):
		return item % self.test_factor == 0

	def do_round(self, monkey_map, common_d):
		for item in self.items:
			# print(item)
			item = (self.inspect(item)) % common_d
			# print(item)
			target = self.true_target if self.test(item) else self.false_target
			monkey_map[target].items.append(item)
		self.items = []


def solve(lst):
	r = 0
	s = set()
	d = {}
	x = 1
	start = 0, 0
	end = 0, 0
	m = [[c for c in l] for l in lst]
	fringe = deque([])
	for i in range(len(m)):
		for j in range(len(m[0])):
			if m[i][j] == 'S':
				start = i, j
				m[i][j] = 'a'
			elif m[i][j] == 'E':
				m[i][j] = 'z'
				end = i, j
	# fringe.append((start, 0, []))

	# while fringe:
	# 	cur, steps, path = fringe.popleft()
	# 	print(cur)
	# 	i, j = cur
	# 	if cur == end:
	# 		print(path)
	# 		return steps
	# 	if cur in s:
	# 		continue
	# 	s.add(cur)
	# 	for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
	# 		d_i, d_j = direction
	# 		n_i, n_j = i + d_i, j + d_j
	# 		if n_i < 0 or n_j < 0 or n_i >= len(m) or n_j >= len(m[0]):
	# 			continue
	# 		if ord(m[n_i][n_j]) - ord(m[i][j]) > 1:
	# 			continue
	# 		n_path = path[:]
	# 		n_path.append((n_i, n_j))
	# 		fringe.append(((n_i, n_j), steps + 1, n_path))
		# fringe.append((start, 0, []))
	fringe.append((end, 0, []))
	while fringe:
		cur, steps, path = fringe.popleft()
		print(cur)
		i, j = cur
		if m[i][j] == 'a':
			print(path)
			return steps
		if cur in s:
			continue
		s.add(cur)
		for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			d_i, d_j = direction
			n_i, n_j = i + d_i, j + d_j
			if n_i < 0 or n_j < 0 or n_i >= len(m) or n_j >= len(m[0]):
				continue
			if ord(m[n_i][n_j]) - ord(m[i][j]) < -1:
				continue
			n_path = path[:]
			n_path.append((n_i, n_j))
			fringe.append(((n_i, n_j), steps + 1, n_path))

	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
