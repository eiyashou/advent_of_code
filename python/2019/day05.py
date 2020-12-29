#!/usr/var/env python3.9

import testfunc as aux
import sys
from intcode import *

def parse(raw):
    return IntCodeMachine(raw)

def one(data):
    data.reset()
    data << 1
    return data.run().pop()

def two(data):
    data.reset()
    data << 5
    return data.run().pop()

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)