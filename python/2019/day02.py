#!/usr/var/env python3.9

import testfunc as aux
import sys
from intcode import *

def parse(raw):
    return IntCodeMachine(raw)

def one(data):
    data.reset()
    data[1] = 12
    data[2] = 2
    return data()[0]

def two(data):
    for i in range(100):
        for j in range(100):
            data.reset()
            data[1] = i
            data[2] = j
            res = data()[0]
            if res == 19690720:
                return 100*i+j

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)