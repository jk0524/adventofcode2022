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
	x = 1
	cycle = 1
	special = [20, 60, 100, 140, 180, 220]
	m = ['.' for _ in range(240)]
	strength = []
	for l in lst:
		if l == 'noop':
			cycle += 1
			# if cycle in special:
			# 	strength.append(cycle * x)
			if abs((cycle - 1) % 40 - x) < 2:
				m[cycle - 1] = '*'
		else:
			val = int(l.split(' ')[1])
			cycle += 1
			# if cycle in special:
			# 	strength.append(cycle * x)
			if abs((cycle - 1) % 40 - x) < 2:
				m[cycle - 1] = '*'
			cycle += 1
			x += val
			# if cycle in special:
			# 	strength.append(cycle * x)
			if abs((cycle - 1) % 40 - x) < 2:
				m[cycle - 1] = '*'
	# r = sum(strength)
	# print(strength)
	for i in range(6):
		print("".join(m[i * 40 : (i + 1) * 40]))
	print(m)
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
