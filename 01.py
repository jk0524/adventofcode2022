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


def solve(lst):
	result = 0
	elf = 0
	s = []
	for l in lst:
		if l:
			elf += int(l)
		else:
			s.append(elf)
			elf = 0
		result = max(elf, result)

	result = sum(sorted(s)[-3:])
	return result

cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
