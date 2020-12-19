import sys, os, re, math, hashlib, itertools, functools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

bin2int = lambda n : int(re.sub(r"[BR]","1",re.sub(r"[FL]","0",n)),2)

def one(raw):
    seats = sorted(map(bin2int, raw.splitlines()))
    return seats[-1]

def two(raw):
    seats = sorted(map(bin2int, raw.splitlines()))
    return (set(range(min(seats),max(seats)+1))-set(seats)).pop()