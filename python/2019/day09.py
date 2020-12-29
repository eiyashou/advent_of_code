#!/usr/var/env python3.9

import testfunc as aux
import sys
from intcode import *

def parse(raw):
    return IntCodeMachine(raw, mem_length=2000)

def one(data):
    data.reset(CLEAR_INPUT,CLEAR_OUTPUT)
    data << 1
    data.run()
    return data.pop()

def two(data):
    data.reset(CLEAR_INPUT,CLEAR_OUTPUT)
    data << 2
    data.run()
    return data.pop()

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)