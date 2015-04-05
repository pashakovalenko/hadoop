#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

for line in sys.stdin:
	#print(line)
	citing, cited = line.strip().split(',')
	if citing.isdigit():
		print('%s\t%s' % (citing, cited))
