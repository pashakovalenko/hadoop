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
		b = []
		for i, j in group:
			t = j.split('\t')
			if t[0] == 'i':
				a.append(t[1])
			elif t[0] == 'o':
				b.append(t[1])
		print('%s\t[%s]\t[%s]\t1\t1' % (word, ','.join(a), ','.join(b)))

if __name__ == '__main__':
	main()