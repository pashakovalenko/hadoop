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
		n = ''
		for i, j in group:
			t = j.split('\t')
			if t[0] == '0':
				n = t[1]
			elif t[0] == '1':
				a.append(t[1])
		if n != '':
			for i in a:
				print('%s\t%s\t' % (i, n))				

if __name__ == '__main__':
	main()