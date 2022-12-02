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

m = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

def solve(lst):
	r = 0
	for l in lst:
		abc = l[0]
		yxz = l[2]
		if yxz == 'Y':
			r += 3
			r += m[abc]
		elif yxz == 'Z':
		 	r += (((m[abc] - 1) + 1) % 3) + 1
		 	r += 6
		else:
			r += (((m[abc] - 1) - 1) % 3) + 1
		print(r)
	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
