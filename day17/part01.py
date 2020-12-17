#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    return int(open("input").readline().strip())

def evaluate(step_size, steps):
    pos = 0
    buf = [0]
    for n in range(steps):
        pos = (pos + step_size) % len(buf) 
        pos += 1
        buf.insert(pos, n + 1)
        #print(pos)
        #print(buf)
    return buf[(pos + 1) % len(buf)]

def main():
    step_size = read_input()
    v = evaluate(step_size, steps=2017)
    print(v)

if __name__ == '__main__':
    main()
