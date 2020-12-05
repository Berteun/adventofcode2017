#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    lines = []
    for l in f:
        lines.append([int(n) for n in l.split()])
    return lines

def get_differences(inp):
    return [max(l) - min(l) for l in inp]

def main():
    inp = read_input()
    diffs = get_differences(inp)
    print(sum(diffs))

if __name__ == '__main__':
    main()
