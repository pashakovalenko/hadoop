#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sys import stdin
import zlib
#import lxml.html
import re
#import lxml

def main():
	for s in stdin:
		t = s.rstrip().split('\t')
		if len(t) != 2:
			continue
		if len(t[1]) < 2000:
			x = t[1][10:].find('/')
			s = t[1][x+10:]
			if s.find('?') >= 0:
				s = s[:s.find('?')]
			print('%s\t0\t%s' % (s.rstrip('/'), t[0]))
			continue

		a = set()
		n = t[0]
		try:
			x = zlib.decompress(t[1].decode('base64')).decode('utf-8').lower()
			SPLIT_RGX = re.compile(r'href ?= ?"[^"]+"', re.U)
			#document = lxml.html.document_fromstring(x)
			#text = " ".join(lxml.etree.XPath("//text()")(document))
			words = re.findall(SPLIT_RGX, x)
			for i in words:
				t = i.split('"')
				if t[1][0] == '/':
					s = t[1]
					if s.find('?') >= 0:
						s = s[:s.find('?')]
					print('%s\t1\t%s\t' % (s.rstrip('/'), n))
		except:
			pass

if __name__ == '__main__':
	main()