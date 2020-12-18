import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def data_parse(data):
    return data.split("\n\n")

def one(raw):
    data = data_parse(raw)
    return sum(len(set(group.replace("\n", ""))) for group in data)

def two(raw):
    data = data_parse(raw)
    return sum(len(set.intersection(*[set(x) for x in group.split("\n")])) for group in data)


test = """
"""