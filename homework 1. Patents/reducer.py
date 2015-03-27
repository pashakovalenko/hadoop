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
	for year, group in groupby(data, itemgetter(0)):
		a = {}
		for y, c in group:
			if c not in a:
				a[c] = 0
			a[c] += 1
		p = list(a.values())
		p.sort()
		m = p[len(p) // 2]
		av = 1.0 * sum(p) / len(p)
		d = 0
		for i in p:
			d += i * i
		d = (1.0 * d / len(p) - av * av) ** (0.5)
		print('%s\t%d\t%d\t%d\t%d\t%f\t%f' % (year, len(p), p[0], m, p[-1], av, d))

main()