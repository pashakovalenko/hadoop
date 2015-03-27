#!/usr/bin/env python
from __future__ import print_function
from sys import stdin

def main():
	for s in stdin:
		if not s.startswith('"'):
			t = s.split(',')
			if len(t) > 4:
				print(t[1] + '\t' + t[4])

main()
