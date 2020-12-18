import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np


def data_parse(raw):
    return [x for x in raw.split("\n")]

def calculate_col(trees, dx, dy, L=0):
    if L == 0: L = len(trees)
    count=0
    x=0
    for line in trees[dy::dy]:
        x+=dx
        if line[x%L] == "#":
            count += 1
    
    return count

def one(raw):
    data = data_parse(raw)
    return calculate_col(data, 3, 1)

def two(raw):
    # raw = test
    data = data_parse(raw)
    L = len(data)
    count = 1
    for dx,dy in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        count *= calculate_col(data, dx, dy, L)
    return count