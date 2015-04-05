#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
from itertools import groupby

splt = lambda line: line.strip().split('\t')

D = 0.85

for citing, group in groupby((splt(line) for line in sys.stdin), lambda line: line[0]):
    citeds = set()
    for cid, cited in group:
        citeds.add(cited)
    print('%s\t%.15f\t[%s]' % (citing,(1-D),','.join(citeds)))
