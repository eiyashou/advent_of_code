#!/usr/var/env python3.9

import testfunc as aux
import sys
from intcode import *
from collections import defaultdict

def parse(raw):
    return IntCodeMachine(raw)

DIR = [(1,0),(0,-1),(-1,0),(0,1)]
MAP_DIR = [(0,-1),(0,1),(-1,0),(1,0)]

def one(droid):

    out = -1
    while out != 2:
        bot << 
        out = 


    return

def two(data):
    return

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)