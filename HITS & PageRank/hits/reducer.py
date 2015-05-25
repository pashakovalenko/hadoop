#!/usr/bin/env python
from __future__ import print_function
from itertools import groupby
from operator import itemgetter
from sys import stdin

def out():
	for s in stdin:
		yield s.rstrip().split('\t', 1)

def main():
	data = out()
	for word, group in groupby(data, itemgetter(0)):
		a = 0
		h = 0
		g = ''
		for i, j in group:
			t = j.split('\t')
			if t[0] == 'h':
				h += int(t[1])
			elif t[0] == 'a':
				a += int(t[1])
			elif t[0] == 'g':
				g = t[1] + '\t' + t[2]
		print('%s\t%s\t%.30d\t%.30d' % (word, g, a, h))

if __name__ == '__main__':
	main()