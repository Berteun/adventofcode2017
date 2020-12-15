#!/usr/bin/env python
# -*- coding: utf-8 -*-
def read_input():
    f = open("input")
    A = int(f.readline().strip().split()[-1])
    B = int(f.readline().strip().split()[-1])
    return A,B


mask = ((1<<16)-1);
def iterate(A, B):
    count = 0 
    for _ in range(40_000_000):
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647
        if ((A & mask) == (B & mask)):
            count += 1
        #print("{:<32d} - {:<32d}".format(A,B))
    return count

def main():
    A, B = read_input()
    print(iterate(A, B))
if __name__ == '__main__':
    main()

