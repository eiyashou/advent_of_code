import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def data_parse(data):
    return sorted(int(x) for x in data.split("\n"))

def one(raw):
    nums = [int(x) for x in raw.split("\n")]
    for num in nums:
        t = 2020-num
        if t in nums:
            return t*num

def one_golf(R):
    N=map(int,R.split("\n"));return [l*c for l in N if (c:=2020-l)in N][0]

def two(raw):
    nums = sorted(int(x) for x in raw.split("\n"))

    for t_ in nums:
        l,r = 0, -1
        t = 2020-t_
        while l<r:
            s = nums[l]+nums[r]
            if s > t:
                r-= 1
            elif s < t:
                l+= 1
            else:
                return nums[l]*nums[r]*t_

def two_golf(R):
    N=map(int,R.split("\n"));return [l*c*r for l in N for r in N if(c:=2020-r-l)in N][0]