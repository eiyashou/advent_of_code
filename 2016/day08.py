import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

sample='''X'''

def parse(raw):
    data = []

    for line in raw.splitlines():
        if bool(p:= re.fullmatch(r"rect (\d+)x(\d+)", line):
            data.append(tuple(map(int, p.groups())))

        elif bool(p:= re.fullmatch(r"rotate (row y|column x)=(\d+) by (\d+))", line):
            data.append((p.group(1)[:-2], int(p.group(2), int(p.group(3)))))
    
    return data


def test(raw):
    data = parse(raw)

    []