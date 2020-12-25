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

def remove_collisions(inp):
    d = {}
    to_remove = set()
    for (i, (p,v,a)) in enumerate(inp):    
        if tuple(p) in d:
            to_remove.add(d[p])
            to_remove.add(i)
        else:
            d[tuple(p)] = i
    return [p for (i, p) in enumerate(inp) if i not in to_remove]

def step(inp):
    for i in range(len(inp)):
        p, v, a = inp[i]
        v = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
        p = (p[0] + v[0], p[1] + v[1], p[2] + v[2])
        inp[i] = (p, v, a)

def main():
    inp = read_input()
    for n in range(40):
        inp = remove_collisions(inp)
        step(inp)
    print("Particles left: {}".format(len(inp)))

if __name__ == '__main__':
    main()
