#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    return [int(l.strip()) for l in f]

def count_steps(offset_list):
    pos = 0
    steps = 0
    while 0 <= pos < len(offset_list):
        offset = offset_list[pos]
        if offset > 2:
            offset_list[pos] -= 1
        else:
            offset_list[pos] += 1
        pos += offset
        steps += 1
    return steps

def main():
    offset_list = read_input()
    print(count_steps(offset_list))

if __name__ == '__main__':
    main()
