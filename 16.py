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

def process(filename):
	f = open(filename, 'r')
	content = f.read()

	return content.splitlines()


def solve(lst):
	r = 0
	s = set()
	d = {}
	flow_map = {}
	non_zero = []
	for l in lst:
		valves = re.findall(r'[A-Z][A-Z]', l)
		d[valves[0]] = valves[1:]
		flow = int(re.findall(r'\d+', l)[0])
		flow_map[valves[0]] = flow
		if flow:
			non_zero.append(valves[0])

	fringe = []
	# heapq.heappush(fringe, (0, 'AA', 0, []))
	# while fringe:
	# 	cost, current_pos, time, open_valves = heapq.heappop(fringe)
	# 	# print(cost, current_pos, time, open_valves)
	# 	if cost < r:
	# 		print(current_pos, time, open_valves, cost)
	# 	r = min(cost, r)

	# 	if (time, current_pos, tuple(open_valves)) in s or time == 30:
	# 		continue
	# 	s.add((time, current_pos, tuple(open_valves)))
	# 	if current_pos not in open_valves and flow_map[current_pos]:
	# 		open_cost = (30 - time - 1) * flow_map[current_pos]
	# 		new_open_values = open_valves[:]
	# 		new_open_values.append(current_pos)
	# 		heapq.heappush(fringe, (cost - open_cost, current_pos, time + 1, new_open_values))

	# 	for n in d[current_pos]:
	# 		heapq.heappush(fringe, (cost, n, time + 1, open_valves[:]))

	# Part 2
	# print(len(d))
	# t = 26
	# i = 0
	# s = defaultdict(lambda: 9999)
	# dic = {}
	# time_set = set()
	# timer = time.time()
	# heapq.heappush(fringe, (0, 'AA', 'AA', 0, []))
	# while fringe:
	# 	cost, current_pos, elephant, ti, open_valves = heapq.heappop(fringe)
	# 	# print(cost, current_pos, elephant, time, open_valves)
	# 	cache_values = tuple(sorted(open_valves))
	# 	i += 1
	# 	# print(i)
	# 	if i % 1000000 == 0:
	# 		print(len(fringe), len(s), len(time_set), time.time() - timer)
	# 		timer = time.time()
	# 	if cost < r:
	# 		print(current_pos, elephant, ti, open_valves, cost)
	# 		# return
	# 	r = min(cost, r)

	# 	if (ti, cache_values) in time_set:
	# 		continue

	# 	opt_cost = cost
	# 	rest = sorted([x for x in non_zero if x not in open_valves], key=lambda x: flow_map[x])
	# 	for j in range(min(len(rest), t - ti)):
	# 		opt_cost -= (t - ti - j) * flow_map[rest[j]]
	# 	if opt_cost >= cost:
	# 		time_set.add((ti, cache_values))
	# 		continue

	# 	if s[(current_pos, elephant, cache_values)] <= ti or ti == t or s[(elephant, current_pos, cache_values)] <= ti:
	# 		continue

	# 	s[(current_pos, elephant, cache_values)] = ti

		

	# 	# if (current_pos, elephant, cache_values) in s or ti == t or (elephant, current_pos, cache_values) in s:
	# 	# 	continue
	# 	s[(current_pos, elephant, cache_values)] = ti
	# 	if current_pos not in open_valves and flow_map[current_pos] and elephant not in open_valves and flow_map[elephant]:
	# 		if current_pos == elephant:
	# 			open_cost = (t - ti - 1) * flow_map[current_pos]
	# 			new_open_values = open_valves[:]
	# 			new_open_values.append(current_pos)
	# 			for n in d[elephant]:
	# 				heapq.heappush(fringe, (cost - open_cost, current_pos, n, ti + 1, new_open_values))
	# 		else:
	# 			open_cost = (t - ti - 1) * flow_map[current_pos] + (t - ti - 1) * flow_map[elephant]
	# 			new_open_values = open_valves[:]
	# 			new_open_values.append(current_pos)
	# 			new_open_values.append(elephant)
	# 			heapq.heappush(fringe, (cost - open_cost, current_pos, elephant, ti + 1, new_open_values))
	# 	if elephant not in open_valves and flow_map[elephant]:
	# 		open_cost = (t - ti - 1) * flow_map[elephant]
	# 		new_open_values = open_valves[:]
	# 		new_open_values.append(elephant)
	# 		for n in d[current_pos]:
	# 			heapq.heappush(fringe, (cost - open_cost, n, elephant, ti + 1, new_open_values))
	# 	if current_pos not in open_valves and flow_map[current_pos]:
	# 		open_cost = (t - ti - 1) * flow_map[current_pos]
	# 		new_open_values = open_valves[:]
	# 		new_open_values.append(current_pos)
	# 		for n in d[elephant]:
	# 			heapq.heappush(fringe, (cost - open_cost, current_pos, n, ti + 1, new_open_values))

	# 	for n in d[current_pos]:
	# 		for e in d[elephant]:
	# 			heapq.heappush(fringe, (cost, n, e, ti + 1, open_valves[:]))

	# squash
	t = 26
	non_zero.append('AA')
	shortest_weights = {}
	for v in non_zero:
		for vv in non_zero:
			if v == vv:
				continue
			shortest_weights[(v, vv)] = bfs(v, vv, d)
	print(shortest_weights)
	s = defaultdict(lambda: 1)

	fringe.append((0, 'AA', 'AA', 0, 0, []))
	while fringe:
		cost, current_pos, elephant, ti, elephant_time, open_valves = fringe.pop()
		# print(cost, current_pos, elephant, ti, elephant_time, open_valves)
		# print(ti * elephant_time)
		cache_values = tuple(sorted(open_valves))
		# cache_values = tuple(open_valves)

		if cost < r:
			print(current_pos, elephant, ti, open_valves, cost)
			# return
		r = min(cost, r)

		if ti == t and elephant_time == t:
			continue

		# if s[(current_pos, elephant, elephant_time, ti, cache_values)] < cost or s[(elephant, current_pos, ti, elephant_time, cache_values)] < cost:
		# 	continue

		s[(current_pos, elephant, elephant_time, ti, cache_values)] = cost
		print(cost, current_pos, elephant, ti, elephant_time, open_valves)
		move_elephant = False
		if not elephant_time == t:
			if elephant not in open_valves and flow_map[elephant]:
				open_cost = (t - elephant_time - 1) * flow_map[elephant]
				new_open_values = open_valves[:]
				new_open_values.append(elephant)
				move_elephant = True
				fringe.append((cost - open_cost, current_pos, elephant, ti, elephant_time + 1, new_open_values))
			for n in non_zero:
				if n == elephant or n in open_valves or n == 'AA':
					continue
				travel = shortest_weights[(elephant, n)]
				if elephant_time + travel + 1 <= t:
					open_cost = (t - elephant_time - travel - 1) * flow_map[n]
					new_open_values = open_valves[:]
					new_open_values.append(n)
					move_elephant = True
					fringe.append((cost - open_cost, current_pos, n, ti, elephant_time + travel + 1, new_open_values))
		if not move_elephant:
			if current_pos not in open_valves and flow_map[current_pos]:
				open_cost = (t - ti - 1) * flow_map[current_pos]
				new_open_values = open_valves[:]
				new_open_values.append(current_pos)
				fringe.append((cost - open_cost, current_pos, elephant, ti + 1, elephant_time, new_open_values))
			for n in non_zero:
				if n == current_pos or n in open_valves or n == 'AA':
					continue
				travel = shortest_weights[(current_pos, n)]
				if ti + travel + 1 <= t:
					open_cost = (t - ti - travel - 1) * flow_map[n]
					new_open_values = open_valves[:]
					new_open_values.append(n)
					fringe.append((cost- open_cost, n, elephant, ti + travel + 1, elephant_time, new_open_values))
		
	return -r

def bfs(start, end, d):
	fringe = deque([])
	s = set()
	fringe.append((start, 0))
	while fringe:
		cur, steps = fringe.popleft()
		if cur == end:
			return steps
		if cur in s:
			continue
		s.add(cur)
		for n in d[cur]:
			fringe.append((n, steps + 1))


cache = dict()

lst = process('input')
x = solve(lst)
print(x)
pyperclip.copy(x)
