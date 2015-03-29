#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


def find(tp):
	print('find', tp.encode('utf-8'))
	f = open('lal.txt', 'r')
	s = f.readline().rstrip()
	while s != '':
		t = s.split()
		#print(t[0].decode('utf-8'))
		if t[0].decode('utf-8') == tp:
			return [int(i) for i in t[1:]]
		s = f.readline().rstrip()
	print("='(")
	return []

def apand(a, b):
	i = 0
	j = 0
	c = []
	while i < len(a) and j < len(b):
		if a[i] == b[j]:
			c.append(a[i])
			i += 1
			j += 1
		elif a[i] < b[j]:
			i += 1
		else:
			j += 1
	return c

def apandnot(a, b):
	i = 0
	j = 0
	c = []
	while i < len(a) or j < len(b):
		if i < len(a) and j < len(b) and a[i] == b[j]:
			i += 1
			j += 1
		elif j == len(b) or i < len(a) and a[i] < b[j]:
			c.append(a[i])
			i += 1
		else:
			j += 1
	return c

def apor(a, b):
	i = 0
	j = 0
	c = []
	while i < len(a) or j < len(b):
		if a[i] == b[j]:
			c.append(a[i])
			i += 1
			j += 1
		elif j == len(b) or i < len(a) and a[i] < b[j]:
			c.append(a[i])
			i += 1
		else:
			c.append(a[j])
			j += 1
	return c

def parse(s):
	s = s.decode('windows-1251') + ' or 777 '
	#t = open('1.txt', 'w')
	#t.write(s)
	#t.close()
	print(s.encode('windows-1251'))
	t = []
	prev = []
	cur = []
	op = 'or'
	pos = 0
	for i in range(len(s)):
		if s[i] == '(':
			p = s[i:].find(')')
			if p < 0:
				raise '123'
			t = parse(s[i + 1 : p])
		elif s[i] == ' ':
			q = s[pos : i]
			if len(q) == 0: 
				pos = i + 1
				continue
			elif q == 'and' or q == u'и':
				op = 'and'
				pos = i + 1
				continue
			elif q == 'or' or q == u'или':
				op = 'or'
				pos = i + 1
				continue
			elif op == 'and' and (q == 'not' or q == u'не'):
				op = 'and not'
				pos = i + 1
				continue
			print(q.encode('utf-8'))
			t = find(q)
		else:
			continue
		if op == 'or':
			prev = apor(prev, cur)
			cur = t
		elif op == 'and':
			cur = apand(cur, t)
		else:
			cur = apandnot(cur, t)
		pos = i + 1
		op = 'and'
		t = []
	return prev

def next():
	s = raw_input()
	p = []
	#try:
	p = parse(s)
	#except:
	#	print('Error while parsing')
		#return
	print(p)

def main():
	while True:
		next()

if __name__ == '__main__':
	main()