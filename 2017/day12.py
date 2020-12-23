#!/usr/bin/env 

# TODO: day12y2017

import libs.aux_funcs as aux
from collections import defaultdict, Counter
import re, math


sample='''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''


with open(f"data/aoc/inputs/2017/day12.txt", "r") as f:
    raw = f.read()


def parse(raw):
    data = defaultdict(list)
    val = set()
    for line in raw.split("\n"):
        if (p:= re.fullmatch(r"(\d+) \<\-\> ([\d, ]+)", line)):
            k = int(p.group(1))
            data[k] += list(n for x in p.group(2).split(",") if (n:= int(x)) != k)
    
    return {k:set(v) for k,v in data.items()}

def recurse(data, keys, ref=set()):
    for k in keys:
        if k not in ref:
            ref = ref | recurse(data, data[k], ref)        
    return ref | set(keys)

def one(data):
    return len(recurse(data, {0}))

def two(data):
    return


if __name__=="__main__":
    print(parse(sample))
    #aux.timeit(one, parse(sample))
    #aux.timeit(two, parse(raw))