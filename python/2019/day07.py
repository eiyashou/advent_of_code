#!/usr/var/env python3.9

import testfunc as aux
from intcode import *
import sys, itertools

def parse(raw):
    return IntCodeMachine(raw)

def one(data):
    ampl = [data.copy() for _ in range(5)] 
    maxm = 0

    for md in itertools.permutations(list(range(0,5)), 5):
        for m, a in zip(md, ampl):
            a.reset()
            a << m

        ampl[0] << 0
        for a1, a2 in zip(ampl, ampl[1:]+ampl[:1]):
            a2 << a1()
        res = ampl[0].feed.pop()

        if res > maxm:
            maxm = res

    return maxm

def two(data):
    ampl = [data.copy() for _ in range(5)] 
    maxm = 0

    for md in itertools.permutations(list(range(5,10)), 5):
        for m, a in zip(md, ampl):
            a.reset(CLEAR_OUTPUT, CLEAR_INPUT)
            a << m

        ampl[0] << 0
        while not all(ampl):
            for a1, a2 in zip(ampl, ampl[1:]+ampl[:1]):
                a2 << a1(halt_on=1)
        res = ampl[0].feed.pop()

        if res > maxm:
            maxm = res

    return maxm

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)