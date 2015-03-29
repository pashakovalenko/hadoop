from __future__ import print_function
import sys
a = sys.stdin.readlines()
a.sort()
for i in a:
	print(i, end='')