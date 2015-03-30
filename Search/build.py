#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

s9s = [[28, 1, 0], [14, 2, 0], [9, 3, 1], [7, 4, 0], [5, 5, 3], [4, 7, 0], [3, 9, 1], [2, 14, 0], [1, 28, 0]]

def encode(w, enctype):
    if enctype == 'simple9':
        return encode_s9(w)
    else:
        return encode_fib(w)

def encode_s9(w):
    l = len(w) + 1
    k = 0
    w += [0] * 28
    res = []
    #print(w)
    while k < l:
        for i in range(len(s9s)):
            flag = True
            for j in range(k, k + s9s[i][0]):
                if w[j] >= 1 << s9s[i][1]:
                    flag = False
                    break
            if not flag:
                continue
            a = i
            for j in range(k, k + s9s[i][0]):
                a = a << s9s[i][1] | w[j]
            a <<= s9s[i][2]
            #print(i, bin(a))
            for j in range(4):
                res.append((a >> ((3 - j) * 8)) & 0xFF)
            k += s9s[i][0]
            break
    return res

def encode_fib(w):
    w = [len(w)] + w
    m = max(w)
    fib = [1, 2]
    while fib[-1] < m:
        fib.append(fib[-1] + fib[-2])
    fib.reverse()
    #print(fib)
    a = []
    for x in w:
        b = [1]
        flag = False
        for i in fib:
            if i <= x:
                x -= i
                b.append(1)
                flag = True
            elif flag:
                b.append(0)
        b.reverse()
        a += b
    #print(a)
    res = []
    a += [0] * 7
    for i in range(len(a) // 8):
        x = 0
        for j in range(i * 8, i * 8 + 8):
            x = (x << 1) | a[j] 
        res.append(x)
    return res                

def main():
    enctype = 'simple9'
    if len(sys.argv) > 2 and ((sys.argv[2] == 'simple9') or (sys.argv[2] == 'fibonacci')):
        enctype = sys.argv[2]
    else:
        print('Usage:\n%s output_dir [simple9 | fibonacci] < reducer_output]' % sys.argv[0])
        return
    #f = open(sys.argv[1], 'r')
    f = sys.stdin
    idx = open(sys.argv[1] + 'index.txt', 'w')
    icp = open(sys.argv[1] + 'index.bin', 'wb')
    pos = 0
    s = f.readline()
    idx.write(enctype + '\n')
    while s != '':
        t = s.split()
        name = t[0]
        t[0] = '0'
        for i in range(len(t)):
            t[i] = int(t[i])
        w = [t[i + 1] - t[i] for i in range(len(t) - 1)]
        #print(w)
        x = encode(w, enctype)
        idx.write(name + ' ' + str(pos) + '\n')
        for i in x:
            icp.write(chr(i))
        pos += len(x)
        #print(name, map(bin, x))
        s = f.readline()
    idx.close()
    icp.close()
    
if __name__ == '__main__':
    main()
