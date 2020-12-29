#!/usr/var/env python3.9

import testfunc as aux
import sys, re

bin2int = lambda n : int(re.sub(r"[BR]","1",re.sub(r"[FL]","0",n)),2)

def parse(raw):
    return sorted(map(bin2int, raw.splitlines()))

def one(data):
    return seats[-1]

def two(data):
    return (set(range(data[0],data[-1]+1))-set(seats)).pop()

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)