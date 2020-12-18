import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def data_parse(raw):
    start, lines = raw.split("\n")
    data = [(i, int(n)) for i, n in enumerate(lines.split("\n")) if n != "x"]
    return start, data


def one(raw):
    # raw = test
    start, data = data_parse(raw)

    earliest = None
    ans = None
    for _, m in data:

        x = m*math.ceil(start/m)-start
        if earliest == None or x > ans:
            ans = m
            earliest = x

    return ans


def two(raw):
    # raw = test
    _, data = data_parse(raw)

    ans = 0
    mod = 1
    for r, m in data:
        rem = m-r
        while ans%m != rem:
            ans += mod
        mod *= m

    return ans%mod  #just in case ans > mod.. which shouldnt be happening but oh well