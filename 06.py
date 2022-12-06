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

def solve(lst):
	r = 0
	s = set()
	d = {}
	l = lst[0]
	for i in range(len(l)):
		s = set([c for c in l[i:i + 14]])
		if len(s) == 14:
			return i + 14
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
