#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

s9s = [[28, 1, 0], [14, 2, 0], [9, 3, 1], [7, 4, 0], [5, 5, 3], [4, 7, 0], [3, 9, 1], [2, 14, 0], [1, 28, 0]]

def find(s):
    #print(s)
    f = open(sys.argv[1], 'r')
    mode = f.readline().rstrip()
    q = f.readline()
    while q != '':
        t = q.split()
        if t[0].decode('utf-8') == s:
            pos = int(t[1])
            f.close()
            if mode == 'simple9':
                return get_idx_s9(pos)
            elif mode == 'fibonacci':
                return get_idx_fib(pos)
        q = f.readline()
    #print('"""')
    return []

def get_idx_s9(pos):
    f = open(sys.argv[2], 'rb')
    f.seek(pos)
    w = []
    while True:
        a = 0
        for i in range(4):
            a = (a << 8) | ord(f.read(1))
            #print(a & 0xFF)
        i = a >> 28
        #print(a, i, bin(a))
        a >>= s9s[i][2]
        t = (1 << s9s[i][1]) - 1
        #print(t)
        b = []
        for j in range(s9s[i][0]):
            b.append(a & t)
            a >>= s9s[i][1]
        #print(b)
        b.reverse()
        for j in b:
            if j == 0:
                a = '&'
                break
            else:
                w.append(j)
        if a == '&':
            break
    f.close()
    for i in range(1, len(w)):
        w[i] += w[i - 1]
    #print(w)
    return w
    
def get_idx_fib(pos):
    f = open(sys.argv[2], 'rb')
    f.seek(pos)
    w = []
    c = 0
    i = 0
    prev = 0
    k = 0
    f1 = 1
    f2 = 2
    while True:
        if i == 0:
            i = 8
            c = ord(f.read(1))
        cur = (c >> 7) & 0x1
        c <<= 1
        i -= 1
        if prev + cur == 2:
            prev = 0
            break
        else:
            k += cur * f1
            f1, f2 = f2, f1 + f2
            prev = cur
    x = 0
    f1 = 1
    f2 = 2
    while k > 0:
        if i == 0:
            i = 8
            c = ord(f.read(1))
        cur = (c >> 7) & 0x1
        c <<= 1
        i -= 1
        if prev + cur == 2:
            w.append(x)
            prev = 0
            x = 0
            f1 = 1
            f2 = 2
            k -= 1
        else:
            x += cur * f1
            f1, f2 = f2, f1 + f2
            prev = cur
    
    f.close()
    for i in range(1, len(w)):
        w[i] += w[i - 1]
    #print(w)
    return w
    
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
        if i < len(a) and j < len(b) and a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
        elif j == len(b) or i < len(a) and a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c

def parse(s):
    #s = s.decode('utf-8', 'ignore').lower() + ' or 777 '
    s += ' '
    t = []
    prev = []
    cur = []
    op = 'or'
    pos = 0
    i = 0
    while i < len(s):
    #for i in range(len(s)):
        t = None
        if s[i] == '(':
            p = s[i:].find(')')
            p += i
            if p < 0:
                raise NameError('Parse error')
            t = parse(s[i + 1 : p])
            i = p
        elif s[i] == ' ':
            q = s[pos : i]
            if len(q) == 0: 
                pos = i + 1
            #    continue
            elif q == 'and' or q == u'и':
                op = 'and'
                pos = i + 1
            #    continue
            elif q == 'or' or q == u'или':
                op = 'or'
                pos = i + 1
            #    continue
            elif op == 'and' and (q == 'not' or q == u'не'):
                op = 'and not'
                pos = i + 1
            #    continue
            #print(q)
            else:
                t = find(q)
        #else:
        #    continue
        if t is not None:
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
        i += 1

    prev = apor(prev, cur)
    return prev

def next():
    print('Я Вас слушаю')
    s = raw_input()
    p = []
    try:
        p = parse(s.decode('utf-8', 'ignore').lower())
    except NameError:
        print('Ошибка распознавания')
        return
    #print(p)
    f = open(sys.argv[3], 'r')
    i = 0
    for j in p:
        while i < j:
            s = f.readline()
            i += 1
        print(s.split()[1])
    f.close()
    print('Итого нашлось урлов: %s' % len(p))

def main():
    if len(sys.argv) < 4:
        print('Usage:\n%s index_list index_binary urls' % sys.argv[0])
        return
    while True:
        next()

if __name__ == '__main__':
    main()
