#!/usr/var/env python3.9

import testfunc as aux
import sys, functools
from collections import Counter

def parse(raw):
    return sorted(int(x) for x in raw.split("\n"))

def one(data):
    nums = Counter(n2-n1 for n1,n2 in zip(data,data[1:]))
    return nums[3] * nums[1]

def two(data):
    data.append(data[-1]+3)

    @functools.lru_cache(max_size=None)
    def iterate(prev):
        if prev == data[-1]:
            return 1
        return sum(iterate(a) for a in data if prev < a <= prev+3)

    return iterate(0)

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)