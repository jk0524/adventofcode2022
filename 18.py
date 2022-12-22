import re
import pyperclip
from collections import defaultdict, deque
import tqdm
import math
import time
import z3
import heapq
from itertools import permutations, product
import numpy as np
import copy
import random
from functools import reduce, cmp_to_key
from operator import mul
from sympy import *
from sympy.solvers import solve


def process(filename):
	f = open(filename, 'r')
	content = f.read()

	return content.splitlines()

class Node:
	def __init__(self, line):
		self.name = line[0]
		l = line[1].split(' ')
		self.parents = l[0], l[2]
		self.op = l[1]

	def result(self, x, y):
		return eval("x " + self.op + " y")

	def expression(self, x, y):
		return "(" + str(x) + ") " + self.op + " (" + str(y) + ")"

  # part 1
def solution(lst):
	r = 0
	s = set()
	d = {}
	left, right, split = defaultdict(int), defaultdict(int), defaultdict(int) 
	nodes = []
	s = set(lst)
	lst = [[int(c) for c in l.split(',')] for l in lst]
	for i in range(len(lst)):
		for j in range(i):
			for x, y, z in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
				if lst[i][x] == lst[j][x] and lst[i][y] == lst[j][y]:
					if abs(lst[i][z] - lst[j][z]) < 2:
						r += 1

	# print(d)

	return len(lst) * 6 - 2 * r


cache = dict()

lst = process('input')
x = solution(lst)
print(x)
pyperclip.copy(x)
