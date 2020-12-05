#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    lines = []
    for l in f:
        lines.append([int(n) for n in l.split()])
    return lines

def get_divisor(l):
    l.sort()
    for (i, d) in enumerate(l):
        j = i + 1
        while j < len(l):
            if l[j] % l[i] == 0:
                return l[j] // l[i]
            j += 1

def get_divisors(inp):
    divisors = [get_divisor(l) for l in inp]
    return divisors

def main():
    inp = read_input()
    divs = get_divisors(inp)
    print(sum(divs))

if __name__ == '__main__':
    main()
