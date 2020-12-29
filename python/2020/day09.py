#!/usr/var/env python3.9

import testfunc as aux
import sys

def parse(raw):
    return [int(x) for x in data.split("\n")]

def two_pointer_sum(nums, t):
    i,j=0,1
    while j < len(nums):
        s = sum(nums[i:j+1])
        if s == t:
            return i,j
        elif s < t:
            j+=1
        else:
            i+=1

def one(nums):
    i = 25
    while True:
        if bool(two_pointer_sum(sorted(nums[i-25:i]), nums[i])): 
            return nums[i]
        i += 1
        
def two(raw):
    invalid = one(raw)
    nums = sorted(data)
    i,j = two_pointer_sum(nums, invalid)
    return nums[i]+nums[j]

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)