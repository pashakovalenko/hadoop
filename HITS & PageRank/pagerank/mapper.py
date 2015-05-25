#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

def main():
	for x in sys.stdin:
		k, w, s = x.split()
		if len(s) == 2:
			continue
		t = s[1:-1].split(',')
		w = float(w) / len(t)
		for i in t:
			print(i + ('\t1\t%.15f' % w))
		print(k + '\t2\t' + s)

if __name__ == '__main__':
	main()