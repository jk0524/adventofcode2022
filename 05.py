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

	# return content.splitlines()
	return content.split('\n\n')

def solve(lst):
	r = 0
	d = {}

	cartes, moves = lst[0], lst[1]
	carts = [line for line in cartes.splitlines()]
	for i in range(1, len(carts[0]), 2):
		cart = [carts[j][i] for j in range(len(carts)) if not carts[j][i] == ' ']
		if cart:
			d[cart[-1]] = cart[0:len(cart)-1][::-1]
	
	for m in moves.splitlines():
		nums = re.findall(r'\d+', m)
		number_crates = int(nums[0])
		src = nums[1]
		dest = nums[2]
		# for _ in range(number_crates):
		# 	box = d[src][-1]
		box = d[src][-number_crates:]
		d[src] = d[src][:len(d[src]) - number_crates]
		d[dest].extend(box)
	print(d)
	r = ''.join([d[str(i)][-1] for i in range(1, 10)])
	

	return r

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
