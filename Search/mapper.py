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
		n = int(t[0])
		x = zlib.decompress(t[1].decode('base64')).decode('utf-8').lower()
		SPLIT_RGX = re.compile(u'[а-я]+', re.U)
		#document = lxml.html.document_fromstring(x)
		#text = " ".join(lxml.etree.XPath("//text()")(document))
		words = re.findall(SPLIT_RGX, x)
		for i in words:
			if len(i) > 1:
				print(i.encode('utf-8') + '\t' + str(n + 1))
		
main()
