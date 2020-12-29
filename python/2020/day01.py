#!/usr/var/env python3.9

import testfunc as aux
import sys

def parse(data):
    return list(map(int, raw.split("\n")))

def one(nums):
    for n in nums:
        if 2020-n in nums:
            return n*(2020-n)

def two(nums):
    for i,n1 in enumerate(nums):
        for n2 in nums[i:]
            if 2020-n1-n2 in nums:
                return n1*n2*(2020-n1-n2)

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)