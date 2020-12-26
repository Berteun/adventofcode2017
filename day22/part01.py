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
            d[(x - offset), (y - offset)] = grid[y][x]
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
    right = 1j
    left = -1j
    if g[pos] == '#':
        d *= right
        g[pos] = '.'
        tinf = False
    else:
        d *= left
        g[pos] = '#'
        tinf = True
    x, y = pos
    pos = (x + int(d.real), y + int(d.imag))
    return pos, d, tinf

def main():
    g = read_input()
    pos = (0, 0)
    d = -1j
    tinf = 0
    for n in range(10_000):
        pos, d, inf = step(g, pos, d)
        tinf += inf
    #print_grid(g, pos)
    print(tinf)

if __name__ == '__main__':
    main()
