#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
import operator

def read_base_input():
    return open("input").readline().strip()

def read_input():
    return [ord(x) for x in open("input").readline().strip()]

def reverse(l, start, r):
    end = (start + (r - 1)) % len(l)
    for _ in range(r // 2):
        l[end], l[start] = l[start], l[end]
        start, end = (start + 1) % len(l),(end - 1) % len(l)

def apply(instr, l, current_pos, skip):
    for i in instr:
        reverse(l, current_pos, i)
        current_pos = (current_pos + i + skip) % len(l)
        skip += 1
    return (l, current_pos, skip)

def dense_hash(inp):
    return [functools.reduce(operator.xor, inp[i * 16:(i + 1)*16]) for i in range(16)]

def to_str(hashl):
    return ''.join("{:02x}".format(n) for n in hashl)

def knot_hash(inp):
    inp = [ord(x) for x in inp] + [17, 31, 73, 47, 23]
    current_pos, skip = 0, 0
    l = list(range(256))
    for _ in range(64):
        l,current_pos,skip = apply(inp, l, current_pos, skip)
    return to_str(dense_hash(l))

m  = {'{:x}'.format(n) : '{:0>4b}'.format(n) for n in range(16) }
print(m)
def map_to_ascii_art(h):
    return ''.join(m[c].replace('0', '.').replace('1', '#') for c in h)

def main():
    base = read_base_input()
    t = 0
    for n in range(128):
        s = '{}-{}'.format(base, n)
        h = knot_hash(s)
        art = map_to_ascii_art(h)
        print(art)
        t += art.count('#')
    print(t)

if __name__ == '__main__':
    main()
