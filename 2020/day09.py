import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def data_parse(raw):
    return [int(x) for x in data.split("\n")]

def one(raw):
    nums = data_parse(raw)
    i = 25
    while True:
        if bool(aux.two_pointer_sum(nums[i-25:i], nums[i])): return nums[i]
        i += 1
        
def two(raw):
    invalid = one(raw)
    nums = sorted(data_parse(raw))
    return aux.two_pointer_sum(nums, invalid)