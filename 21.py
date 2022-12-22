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

def solution(lst):
	r = 0
	r = 1
	s = set()
	d = {}
	
	nodes = []
	s = set(lst)
	init_printing(use_unicode=True)

	for l in lst:
		l = l.split(': ')
		# print(l[0], l[1])
		if l[1][0].isalpha():
			nodes.append(Node(l))
		else:
			if l[0] == 'humn':
				d[l[0]] = 'x'
			else:
				d[l[0]] = int(l[1])


	while 'root' not in d:
		for n in nodes:
			if n.name in d:
				continue
			elif n.parents[0] in d and n.parents[1] in d:
				if n.name == 'root':
					expr0 = d[n.parents[0]]
					expr1 = d[n.parents[1]]
					x = symbols('x')
					return int(solve(expr0 + " - " + expr1)[0])
					# print(simplify(eval(expr0)))
					# print(simplify(eval(expr1)))
					# return 0
					

				else:
					d[n.name] = n.expression(d[n.parents[0]], d[n.parents[1]])

	# print(d)

	return r


cache = dict()

lst = process('input')
x = solution(lst)
print(x)
pyperclip.copy(x)
