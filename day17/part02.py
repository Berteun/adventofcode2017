#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    return int(open("input").readline().strip())

def evaluate(step_size, steps):
    pos = 0
    for n in range(1, steps + 1):
        pos = (pos + step_size) % n + 1
        if pos == 1:
            out_value = n
    return out_value

def main():
    step_size = read_input()
    v = evaluate(step_size, steps=50000000)
    print(v)

if __name__ == '__main__':
    main()
