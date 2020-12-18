import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np


def data_parse(raw):
    data = [int(x) for x in raw.splitlines()]
    return data


def one(raw):
    data = data_parse(raw)

    return sum(data)


def two(raw):
    data = data_parse(_)
    L = len(data)

    f = 0
    i = -1

    prev = {0}

    while True:
        f += data[(i:=(i+1)%L)]

        if f in prev:
            return f
        else:
            prev.add(f)