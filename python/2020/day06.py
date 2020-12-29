#!/usr/var/env python3.9

import testfunc as aux
import sys

def parse(data):
    return data.split("\n\n")

def one(data):
    return sum(len(set(group.replace("\n", ""))) for group in data)

def two(data):
    return sum(len(set.intersection(*[set(x) for x in group.split("\n")])) for group in data)

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)