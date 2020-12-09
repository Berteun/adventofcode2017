#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    return [int(x) for x in open("input").readline().strip().split(",")]

def reverse(l, start, r):
    end = (start + (r - 1)) % len(l)
    for _ in range(r // 2):
        l[end], l[start] = l[start], l[end]
        start = (start + 1) % len(l)
        end = (end - 1) % len(l)

def apply(instr, l):
    current_pos = 0
    skip = 0
    for i in instr:
        reverse(l, current_pos, i)
        current_pos = (current_pos + i + skip) % len(l)
        skip += 1
    return l

def main():
    inp = read_input()
    res = apply(inp, list(range(256)))
    print(res)
    print(res[0] * res[1])

if __name__ == '__main__':
    main()
