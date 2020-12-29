#!/usr/var/env python3.9

import testfunc as aux
import sys
#from collections import defaultdict

def parse(raw):
    return [x for x in raw.split("\n")]

def calculate_col(trees, dx, dy):
    count=0
    x=0
    for line in trees[dy::dy]:
        x+=dx
        if line[x%len(line)] == "#":
            count += 1
    return count

def one(data):
    return calculate_col(data, 3, 1)

def two(data):
    count = 1
    for dx,dy in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        count *= calculate_col(data, dx, dy)
    return count

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)