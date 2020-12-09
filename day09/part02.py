#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    return [l.strip() for l in f]

def score(l):
    depth = 0
    state = 'OPEN'
    score = 0
    p = 0
    garb = 0
    while p < len(l):
        c = l[p]
        if state == 'OPEN':
            if c == '{':
                depth += 1
            elif c == '<':
                state = 'GARB'
            elif c == '}':
                score += depth
                state = 'CING'
                depth -= 1
        elif state == 'GARB':
            if c == '>':
                state = 'CING'
            elif c == '!':
                state = 'IGNR'
            else:
                garb += 1
        elif state == 'IGNR':
            state = 'GARB'
        elif state == 'CING':
            if c == ',':
                state = 'OPEN'
            elif c == '}':
                score += depth
                depth -= 1
        p += 1            
    return garb

def main():
    inp = read_input()
    #inp = ['{}','{{{}}}','{{},{}}','{<a>,<a>,<a>,<a>}','{{<ab>},{<ab>},{<ab>},{<ab>}}','{{<!!>},{<!!>},{<!!>},{<!!>}}','{{<a!>},{<a!>},{<a!>},{<ab>}}']
    s = sum(score(l) for l in inp)
    print(s)

if __name__ == '__main__':
    main()

