#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    return [l.strip().split(' ') for l in f]

def is_valid(passphrase):
    return len(set(passphrase)) == len(passphrase)

def main():
    inp = read_input()
    print(sum(is_valid(passphrase) for passphrase in inp))

if __name__ == '__main__':
    main()
