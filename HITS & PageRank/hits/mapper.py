#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sys import stdin

def main():
	for s in stdin:
		t = s.rstrip().split('\t')
		if len(t) != 5:
			continue
		a = t[1][1:-1].split(',')
		for i in a:
			print('%s\t%s\t%s' % (i, 'h', t[3]))
		b = t[2][1:-1].split(',')
		for i in b:
			print('%s\t%s\t%s' % (i, 'a', t[4]))
		print('%s\t%s\t%s\t%s' % (t[0], 'g', t[1], t[2]))	

if __name__ == '__main__':
	main()