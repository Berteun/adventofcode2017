#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

def read_input():
    grid = [list(l.strip()) for l in open("input")]
    offset = len(grid) // 2
    d = defaultdict(lambda: ".")

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            d[(x - offset) * 1 +  (y - offset)*1j] = grid[y][x]
    return d

def print_grid(g, pos):
    for y in range(-4, 5):
        for x in range(-4, 5):
            if (x, y) == pos:
                sys.stdout.write("[{}]".format(g[pos]))
            else:
                sys.stdout.write(" {} ".format(g[(x,y)]))
        sys.stdout.write("\n")
    print("")

def step(g, pos, d):
    tinf = False
    if g[pos] == '#':
        d *= 1j
        g[pos] = 'F'
    elif g[pos] == 'W':
        g[pos] = '#'
        tinf = True
    elif g[pos] == 'F':
        d = -d
        g[pos] = '.'
    else: # Clean
        d *= -1j
        g[pos] = 'W'
    return pos + d, d, tinf

def main():
    g = read_input()
    pos = 0 + 0j
    d = -1j
    tinf = 0
    for n in range(10000000):
        pos, d, inf = step(g, pos, d)
        tinf += inf
        #print_grid(g, pos)
    print(tinf)

if __name__ == '__main__':
    main()
