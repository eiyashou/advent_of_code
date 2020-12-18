import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np


def data_parse(raw):
    data = [int(x) for x in raw.split("\n")]
    return data


def one(raw):
    # raw = test
    data = data_parse(raw)
    data.sort()

    nums = Counter(data[i] - data[i-1] for i in range(1, len(data)))

    return nums[3] * nums[1]


def two(raw):
    data = data_parse(raw)
    data.sort()
    data.append(data[-1]+3)

    @func_tools.lru_cache(max_size=None)
    def iterate(prev):
        if prev == data[-1]:
            return 1
        
        return sum(iterate(a) for a in data if prev < a <= prev+3)

    return iterate(0)


test = """"""