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
	for l in lst:
		if l == '$ cd /':
			cur = root
		elif l == '$ cd ..':
			cur = cur.parent
		elif l[:5] == '$ cd ':
			name = l[5:]
			n = Node(0, name, True, cur)
			cur.children.append(n)
			cur = n
		elif l == '$ ls':
			continue
		else:
			file = l.split(' ')
			if file[0].isalpha():
				continue
			n = Node(int(file[0]), file[1], False, cur)
			cur.children.append(n)
	# r = sum([f.total_size() for f in root.all_folders() if f.total_size() <= 100000])
	free = 30000000 - (70000000 - root.total_size())
	r = min([f.total_size() for f in root.all_folders() if f.total_size() >= free])
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
