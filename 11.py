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

	# return content.splitlines()
	return content.split('\n\n')

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

	def do_round(self, monkey_map):
		for item in self.items:
			# print(item)
			item = (self.inspect(item)) % 9699690
			# print(item)
			target = self.true_target if self.test(item) else self.false_target
			monkey_map[target].items.append(item)
		self.items = []


def solve(lst):
	r = 0
	s = set()
	d = {}
	x = 1
	
	for l in lst:
		m = Monkey(l)
		d[m.id] = m
	for j in range(10000):
		print('round', j)
		for i in sorted(d.keys()):
			# print(i)
			m = d[i]
			m.do_round(d)

	cnts = sorted([m.cnt for m in d.values()])[::-1]
	print(reduce(mul, [m.test_factor for m in d.values()]))
	# print(d)
	print(cnts)
	r = cnts[0] * cnts[1]
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
