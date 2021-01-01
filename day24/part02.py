#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    components = []
    for l in open("input"):
        l = l.strip()
        f, t = l.split("/")
        components.append((int(f), int(t)))
    return components

cache = {}

def build_bridge_h(bridge, nodes):
    key = (bridge[-1], nodes)

    #   print(bridge, nodes)
    if (bridge[-1], nodes) in cache:
        return cache[key]
    if not nodes:
        return bridge

    bridges = [bridge]
    for (t,f) in nodes:
        nnodes = nodes.difference({(t,f)})
        if bridge[-1] == f:
            b = build_bridge_h(bridge + [f, t], nnodes)
            bridges.append(b)
        if bridge[-1] == t:
            b = build_bridge_h(bridge + [t, f], nnodes)
            bridges.append(b)
    cache[key] = max((len(b), sum(b), b) for b in bridges)[2]
    return cache[key]

def build_bridge(inp):
    nodes = frozenset(inp)
    bridges = []
    for (f,t) in nodes:                
        bridge = [f,t] 
        if (f == 0):
            nnodes = nodes.difference({(f,t)})
            bridges.append(build_bridge_h([f,t], nnodes))
        if (t == 0):
            nnodes = nodes.difference((f,t))
            bridges.append(build_bridge_h([t,f], nnodes))
    return max((len(b), sum(b), b) for b in bridges)

def main():
    inp = read_input()
    print(build_bridge(inp)[1])

if __name__ == '__main__':
    main()
