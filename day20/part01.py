#!/usr/bin/env python
# -*- coding: utf-8 -*-

def split(x):
    return [int(n) for n in x[3:-1].split(",")]

def read_input():
    f = open("input")
    particles = []
    for l in f:
        p, v, a = l.strip().split(", ")
        particles.append((split(p), split(v), split(a)))
    return particles

def d(t):
    return (t[0]**2 + t[1]**2 + t[2]**2)**(.5)

def main():
    inp = read_input()
    # The particle that accelerates slowest stays closest in the end
    print(min((d(a), i) for i, (p,v,a) in enumerate(inp))[1])

if __name__ == '__main__':
    main()
