#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

def read_input():
    g = defaultdict(list)
    for l in open("input"):
        source, targets = l.strip().split(' <-> ')
        targets = targets.split(", ")
        g[source].extend(targets)
    return g


def dfs(g, cur, seen):
    for n in g[cur]:
        if not n in seen:
            seen.add(n)
            dfs(g, n, seen)

def main():
    g = read_input()
    seen = {'0'}
    dfs(g, '0', seen)
    print(len(seen))
    
if __name__ == '__main__':
    main()
