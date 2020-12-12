#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Triple:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Triple(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Triple(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self):
        return (abs(self.x) + abs(self.y) + abs(self.z))//2

    def __str__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)

def read_input():
    return open("input").readline().strip().split(",")

def map_to_coord(inp):
    m = {
        # First axis
        "nw": Triple( 0,-1,+1),
        "se": Triple( 0, 1,-1),
        # Second axis
        "ne": Triple( 1, 0,-1),
        "sw": Triple(-1, 0,+1),
        # Thirds axis
        "n":  Triple( 1,-1, 0),
        "s":  Triple(-1, 1, 0),
    }
    return m[inp]

def walk(inp):
    coord = Triple()
    m = abs(coord)
    for i in inp:
        coord = coord + map_to_coord(i)
        m = max(abs(coord),m)
    return m

def main():
    inp = read_input()    
    #inp = ["ne","ne","s","s"]
    #inp = ["ne","ne","ne"]
    #inp = ["se","sw","se","sw","sw"]
    final = walk(inp)
    print(final)

if __name__ == '__main__':
    main()
