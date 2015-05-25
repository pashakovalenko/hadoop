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
		a = []
		for i, j in group:
			a.append(j)
		print('%s\t1\t[%s]' % (word, ','.join(a)))

if __name__ == '__main__':
	main()