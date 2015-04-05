#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

def main():
	D = 0.85
	p = ''
	v = 1 - D
	g = '[]'
	for x in sys.stdin:
		a, t, b = x.split()
		if a != p:
			if p != '':
				print(p + ('\t%.15f\t' % v) + g)
			p = a
			v = 1 - D
			g = '[]'
		if t == '1':
			v += float(b) * D
		else:
			g = b
	print(p + ('\t%.15f\t' % v) + g)
		
if __name__ == '__main__':
	main()