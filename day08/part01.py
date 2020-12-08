#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple, defaultdict
import operator

Operation = namedtuple('Operation', ['reg', 'action', 'amount', 'cond_reg', 'condition', 'constraint'])
def read_input():
    operations = []
    for l in open("input"):
        r = l.strip().split()
        if r[1] == 'inc':
            action = operator.add
        else:
            action = operator.sub

        if r[5] == '<':
            cond = operator.lt
        elif r[5] == '<=':
            cond = operator.le
        elif r[5] == '>':
            cond = operator.gt
        elif r[5] == '>=':
            cond = operator.ge
        elif r[5] == '==':
            cond = operator.eq
        elif r[5] == '!=':
            cond = operator.ne
        op = Operation(r[0], action, int(r[2]), r[4], cond, int(r[6]))
        operations.append(op)
    return operations

def execute(ops):
    regs = defaultdict(int)
    for op in ops:
        if op.condition(regs[op.cond_reg], op.constraint):
            regs[op.reg] = op.action(regs[op.reg], op.amount)
    return regs

def find_max(regs):
    return max(regs.values())

def main():
    ops = read_input()
    regs = execute(ops)
    print(find_max(regs)) 

if __name__ == '__main__':
    main()
