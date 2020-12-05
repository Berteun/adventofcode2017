#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    return f.readline().strip()

def find_matching_numbers(inp):
    matches = 0
    for (i, c) in enumerate(inp):
        if c == inp[(i + 1) % len(inp)]:
            matches += int(c)
    return matches


def main():
    inp = read_input()
    print(find_matching_numbers(inp))

if __name__ == '__main__':
    main()
