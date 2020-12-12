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
    all_nodes = set(g.keys())
    groups = 0
    while all_nodes:
        groups += 1
        start = all_nodes.pop()
        seen = {start}
        dfs(g, start, seen)
        print(groups, start, len(seen))
        all_nodes.difference_update(seen)
    print(groups)
    
if __name__ == '__main__':
    main()
