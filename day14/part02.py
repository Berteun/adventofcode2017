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
def map_to_ascii_art(h):
    return ''.join(m[c].replace('0', '.').replace('1', '#') for c in h)

def flood_fill(disk_map, y, x):
    disk_map[y][x] = '@'
    if x + 1 < len(disk_map[y]) and disk_map[y][x + 1] == '#':
        flood_fill(disk_map, y, x + 1)
    if y + 1 < len(disk_map) and disk_map[y + 1][x] == '#':
        flood_fill(disk_map, y + 1, x)
    if y - 1 >= 0 and disk_map[y - 1][x] == '#':
        flood_fill(disk_map, y - 1, x)
    if x - 1 >= 0 and disk_map[y][x - 1] == '#':
        flood_fill(disk_map, y, x - 1)

def print_map(disk_map):
    print('\n'.join(''.join(l) for l in disk_map))
    print('--------')

def count_regions(disk_map):
    regions = 0
    for (y,l) in enumerate(disk_map):
        for (x,c) in enumerate(l):
            if disk_map[y][x] == '#':
                regions += 1
                flood_fill(disk_map, y, x)
                #print_map(disk_map)
    return regions

def main():
    base = read_base_input()
    disk_map = []
    for n in range(128):
        s = '{}-{}'.format(base, n)
        h = knot_hash(s)
        art = map_to_ascii_art(h)
        disk_map.append(list(art))
    print(count_regions(disk_map))

if __name__ == '__main__':
    main()
